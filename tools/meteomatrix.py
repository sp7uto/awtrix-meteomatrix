#!/usr/bin/env python3
"""MeteoMatrix AWTRIX NG installer. Python >=3.9, standard library only.

All write operations require --apply. Existing scripts are updated only through
the conditional script-update endpoint. No other apps are modified.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "src" / "MeteoMatrix.ax"
NAME_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,32}$")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def request(base, path, method="GET", body=None, user=None, password=None):
    headers = {}
    if body is not None:
        headers["Content-Type"] = "application/json" if isinstance(body, dict) else "text/plain; charset=utf-8"
        if isinstance(body, dict):
            body = json.dumps(body).encode("utf-8")
    if user is not None:
        import base64
        token = base64.b64encode((user + ":" + (password or "")).encode()).decode()
        headers["Authorization"] = "Basic " + token
    req = Request(base.rstrip("/") + path, data=body, headers=headers, method=method)
    try:
        with urlopen(req, timeout=15) as response:
            return response.status, response.read()
    except HTTPError as err:
        return err.code, err.read()


def parse_response(status, body):
    if status != 200:
        raise RuntimeError("AWTRIX returned HTTP " + str(status) + ": " + body.decode("utf-8", "replace")[:500])
    try:
        obj = json.loads(body)
    except (ValueError, UnicodeError) as exc:
        raise RuntimeError("Expected JSON response from AWTRIX") from exc
    if obj.get("ok") is not True or obj.get("error") is not None:
        raise RuntimeError("AWTRIX reported an application error: " + str(obj.get("error")))
    return obj


def backup(data, name, folder):
    folder.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = folder / (name + "-" + stamp + "-" + digest(data)[:12] + ".ax")
    with dest.open("xb") as f:
        f.write(data)
    os.chmod(dest, 0o600)
    return dest


def get_script(base, name, auth):
    status, payload = request(base, "/api/v1/apps/script/" + name, **auth)
    if status == 404:
        return None
    if status != 200:
        raise RuntimeError("Cannot read current script: HTTP " + str(status))
    return payload


def run(args):
    if not NAME_PATTERN.fullmatch(args.name):
        raise ValueError("Invalid AWTRIX application name")
    auth = {"user": args.user, "password": os.environ.get("AWTRIX_PASSWORD")}
    if args.user and auth["password"] is None:
        raise ValueError("Set AWTRIX_PASSWORD in your terminal; do not put passwords in command arguments")
    base = args.host
    if not base.startswith(("http://", "https://")):
        base = "http://" + base
    previous = get_script(base, args.name, auth)
    if args.command == "status":
        print("App:", args.name, "| installed:", previous is not None)
        if previous is not None:
            print("Device SHA256:", digest(previous))
        return
    if args.command == "backup":
        if previous is None:
            raise RuntimeError("Script not installed; no backup available")
        dest = backup(previous, args.name, args.backup_dir)
        print("Backup:", dest, "| SHA256:", digest(previous))
        return
    if args.command == "restore":
        if not args.apply:
            print("DRY RUN: restore requires --apply")
            return
        if previous is None:
            raise RuntimeError("Restore target does not exist; refusing to create it implicitly")
        restored = args.file.read_bytes()
        if not restored:
            raise ValueError("Empty restore source")
        dest = backup(previous, args.name, args.backup_dir)
        print("Pre-restore backup:", dest)
        st, res = request(base, "/api/v1/apps/script-update/" + args.name, method="PUT",
                          body={"expected_source": previous.decode("utf-8"), "source": restored.decode("utf-8")}, **auth)
        parse_response(st, res)
        confirmed = get_script(base, args.name, auth)
        if confirmed != restored:
            raise RuntimeError("Restore verification mismatch")
        print("RESTORED:", digest(restored))
        return

    source = args.file.read_bytes()
    if not source or b"# @name MeteoMatrix" not in source:
        raise ValueError("Source does not look like a MeteoMatrix Berry application")
    if previous == source:
        print("Already up to date:", digest(source))
        return
    print("New SHA256:", digest(source))
    print("Mode:", "conditional update" if previous is not None else "new independent app")
    if not args.apply:
        print("DRY RUN: no changes made; rerun with --apply to install")
        return
    if previous is not None:
        dest = backup(previous, args.name, args.backup_dir)
        print("Pre-install backup:", dest)
        path = "/api/v1/apps/script-update/" + args.name
        body = {"expected_source": previous.decode("utf-8"), "source": source.decode("utf-8")}
    else:
        # Atomic create: do not overwrite a script created after the initial GET.
        path = "/api/v1/apps/script-update/" + args.name
        body = {"expected_source": None, "source": source.decode("utf-8")}
    status, payload = request(base, path, method="PUT", body=body, **auth)
    try:
        parse_response(status, payload)
        actual = get_script(base, args.name, auth)
        if actual != source:
            raise RuntimeError("Read-back SHA256 mismatch")
    except Exception:
        print("Install was not confirmed. Automatic rollback is intentionally disabled", file=sys.stderr)
        print("to avoid deleting or overwriting an app after a response/connection ambiguity.", file=sys.stderr)
        print("Inspect device state, then use 'restore --file BACKUP --apply' if needed.", file=sys.stderr)
        raise
    print("SUCCESS: installed and read-back verified:", digest(source))


def main():
    parser = argparse.ArgumentParser(description="Safe MeteoMatrix installer for AWTRIX NG")
    parser.add_argument("command", choices=["status", "backup", "install", "restore"])
    parser.add_argument("--host", required=True, help="AWTRIX host or URL; must be reachable from this computer")
    parser.add_argument("--name", default="MeteoMatrix", help="AWTRIX script ID (default MeteoMatrix)")
    parser.add_argument("--file", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--user", help="AWTRIX HTTP basic-auth username; password read from AWTRIX_PASSWORD")
    parser.add_argument("--backup-dir", type=Path, default=ROOT / "backups")
    parser.add_argument("--apply", action="store_true", help="Explicitly allow modifying the device")
    args = parser.parse_args()
    try:
        run(args)
    except (ValueError, RuntimeError, OSError, URLError, UnicodeError) as exc:
        parser.exit(1, "ERROR: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
