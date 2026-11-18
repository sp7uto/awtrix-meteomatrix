![MeteoMatrix — Ulanzi TC001](docs/images/hero-meteomatrix.png)

# MeteoMatrix — weather, air quality & astronomy for AWTRIX NG

[Polski](docs/PL.md) · [English documentation](docs/EN.md)

**Latest published release: [v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/tag/v1.0.0-rc1)** — public release candidate, not stable v1.0.0.

MeteoMatrix brings weather and environmental data to **AWTRIX NG / Ulanzi TC001 (32×8)**. It is derived from the maintainer-verified **SieradzMeteo v1.6** and preserves its approved pixel art, 26 pages and Sun/Moon animations.

## Features

- Current and feels-like temperatures, rainfall, snowfall, cloud cover, wind and pressure.
- European AQI, PM2.5, PM10 and seasonal pollen.
- Sunrise and sunset, moonrise and moonset, lunar phase.
- Original pixel-art icons and animated astronomical scenes.
- Hiding of selected zero values, while still displaying temperature.
- Latitude, longitude, timezone and PL/EN display-language configuration.

## Download and installation

**[Download MeteoMatrix.ax](https://github.com/sp7uto/awtrix-meteomatrix/releases/download/v1.0.0-rc1/MeteoMatrix.ax)** · [SHA-256](https://github.com/sp7uto/awtrix-meteomatrix/releases/download/v1.0.0-rc1/MeteoMatrix.ax.sha256)

The maintainer has confirmed successful installations on a physical **TC001** through **both the AWTRIX NG web interface and the Python installer**. In-place upgrades and restoration/rollback still require separate verification.

Read the [English installation guide](docs/INSTALL_EN.md) or [Polish installation guide](docs/INSTALL_PL.md). The Python tool performs a read-only check by default and requires `--apply` for changes.

## Original and current sources

- [MeteoMatrix Berry source](src/MeteoMatrix.ax)
- [Verified SieradzMeteo v1.6 original](src/legacy/SieradzMeteo_v1_6.ax)
- [Python installer](tools/meteomatrix.py)
- [Release notes](release/notes-v1.0.0-rc1.md)
- [Development checklist](docs/DEVELOPMENT.md)

## Visual overview

![MeteoMatrix features](docs/images/features-grid.svg)

![Architecture — Open-Meteo to AWTRIX NG](docs/images/how-it-works.svg)

These are project illustrations rather than screenshots of the running device. Open-Meteo pollen availability varies by location and season.

**Licensing:** An open-source license has not yet been published; public source availability does not itself grant redistribution rights.
