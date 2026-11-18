# MeteoMatrix installation — development build

> **Warning:** `src/MeteoMatrix.ax` is a preliminary adaptation of the preserved SieradzMeteo v1.6 source. The MeteoMatrix adaptation has been installed and confirmed working on a physical TC001 by the maintainer. It is **not a stable release**. PL/EN display labels have been added but are untested on hardware; v1.6 astronomy animations are imported and awaiting hardware validation.

## Requirements

- AWTRIX NG with Berry scripting enabled.
- Python 3.9+ on a computer with network access to the device.
- A checkout of `sp7uto/awtrix-meteomatrix`.
- If AWTRIX HTTP authentication is enabled, pass the username using `--user` and the password via the `AWTRIX_PASSWORD` environment variable.

## Read-only checks

```bash
python3 tools/meteomatrix.py status --host YOUR_AWTRIX_IP
python3 tools/meteomatrix.py install --host YOUR_AWTRIX_IP
```

Without `--apply`, installation and restoration only report what they would do. The default app ID is **MeteoMatrix**, separate from any existing SieradzMeteo app.

## Test deployment (only after source approval)

```bash
python3 tools/meteomatrix.py install --host YOUR_AWTRIX_IP --apply
```

On the Scripts page, configure Latitude, Longitude and Timezone with the app settings gear ⚙. The Sieradz defaults are examples only.

## Backup and recovery

```bash
python3 tools/meteomatrix.py backup --host YOUR_AWTRIX_IP
python3 tools/meteomatrix.py restore --host YOUR_AWTRIX_IP --file backups/YOUR-BACKUP.ax
python3 tools/meteomatrix.py restore --host YOUR_AWTRIX_IP --file backups/YOUR-BACKUP.ax --apply
```

The tool saves a timestamped previous source with a SHA-256 suffix before updating. Existing apps are changed only using the conditional `script-update` API endpoint, never with a blind overwrite.

When an installation response is ambiguous, the tool does **not** roll back automatically. Check device status and restore a known-good backup explicitly. A newly installed failing app may need manual removal through AWTRIX NG's web interface.

## Local checks

```bash
python3 -m unittest discover -s tests -v
```

The installer does not change firmware, Wi-Fi, MQTT or unrelated scripts.


## Verified installation methods

2026-11-19: the maintainer confirmed working installs through both the Python installer and the AWTRIX NG web panel on TC001. Upgrading an existing app and backup restoration remain separate tests.
