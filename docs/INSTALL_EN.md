# MeteoMatrix v1.0.0-rc1 installation

> **Status:** [v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/tag/v1.0.0-rc1) is the published release candidate, based on the verified SieradzMeteo v1.6. The maintainer confirmed MeteoMatrix works on TC001 after installation by Python and the AWTRIX NG web UI. Update-in-place and backup restoration still require dedicated testing.

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

## Install the RC1 build

```bash
python3 tools/meteomatrix.py install --host YOUR_AWTRIX_IP --apply
```

On the Scripts page, configure Latitude, Longitude, Timezone and Language with the app settings gear ⚙. The Sieradz defaults are examples only.

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
