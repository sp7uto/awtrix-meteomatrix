# MeteoMatrix — Weather, Air Quality & Astronomy for AWTRIX NG

[English](README_EN.md) · [Polski](docs/PL.md)

MeteoMatrix is a planned open-source, location-configurable weather and environment application for **AWTRIX NG** and **Ulanzi TC001 (32×8)**, derived from the original **SieradzMeteo** project.

> **Status: development preview. No installable Berry (.ax) release has been published.**

## Scope
- Weather, feels-like temperature, precipitation, wind, cloud cover and pressure.
- European air quality index, PM2.5, PM10 and seasonal pollen.
- Sunrise/sunset, moonrise/moonset and moon phase.
- Approved original pixel-art icons and animated rise/set scenes.
- Hide agreed zero-valued measurements (temperature always shown).
- Configurable latitude, longitude, timezone and Polish/English display language.
- Open-Meteo as the data source.
- Versioned GitHub releases, verified installer and reversible updates **after device API testing**.

Sieradz (51.590748, 18.736974, Europe/Warsaw) is a sample configuration only; no private LAN address or API credentials are part of the project.

## Roadmap
1. Import and verify the actual SieradzMeteo Berry code and its approved artwork.
2. Make location and language configurable without changing visual behavior.
3. Validate firmware settings and installation endpoints on AWTRIX NG.
4. Implement backup, integrity verification and rollback.
5. Test on TC001, then publish versioned release assets and installation instructions.

## Documentation
- [Polska dokumentacja](docs/PL.md)
- [English guide](README_EN.md)
- [Development and release policy](docs/DEVELOPMENT.md)
- [Changelog](CHANGELOG.md)

No license is included at this stage; publishing source does not yet grant permission to redistribute or modify it. The license will be selected before the first public installable release.

Not affiliated with AWTRIX NG or Open-Meteo.


## Visual overview

![MeteoMatrix features](docs/images/features-grid.svg)

**Features at a glance:** weather, temperature, air quality, pollen, Sun and Moon, configurable location.

![MeteoMatrix architecture](docs/images/how-it-works.svg)

**Architecture:** Open-Meteo APIs → Berry script → AWTRIX NG display. These are feature illustrations, not screenshots of a released device build.

**Hero artwork:** the approved photorealistic TC001 banner is retained separately until its original PNG can be uploaded unchanged. It will not be replaced with an imitation.
