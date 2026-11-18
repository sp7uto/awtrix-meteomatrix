# Installation

[[← Introduction|EN-Introduction]] · [[Configuration →|EN-Configuration]]

## Requirements

- Ulanzi TC001 with AWTRIX NG and Berry scripting.
- Browser access to the AWTRIX NG web UI.
- The published `MeteoMatrix.ax` app.

## Install through AWTRIX NG

1. Download [MeteoMatrix.ax (v1.0.0-rc1)](https://github.com/sp7uto/awtrix-meteomatrix/releases/download/v1.0.0-rc1/MeteoMatrix.ax).
2. Open your AWTRIX NG web interface.
3. Upload the Berry script using the scripts management section.
4. Start the app and configure your location and language.

## Install using Python

Requires Python 3.9+ and a checkout of the repository. Run in its root directory:

```bash
python3 tools/meteomatrix.py status --host YOUR_AWTRIX_IP
python3 tools/meteomatrix.py install --host YOUR_AWTRIX_IP
```

Both commands are read-only by default. To explicitly install:

```bash
python3 tools/meteomatrix.py install --host YOUR_AWTRIX_IP --apply
```

Both installation methods have been confirmed working on a physical TC001. Upgrade-in-place and backup restoration require separate device verification.

[Full installation guide](https://github.com/sp7uto/awtrix-meteomatrix/blob/main/docs/INSTALL_EN.md).
