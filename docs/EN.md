![MeteoMatrix — project banner for AWTRIX NG](images/hero-meteomatrix.png)

# MeteoMatrix — English documentation

## Project status

This is a **development preview**. A development Berry `.ax` adaptation is published, but it has not been hardware-tested and is not a stable release. Do not replace a working weather application with this repository scaffold.

## Purpose

MeteoMatrix will provide weather and environment information for an AWTRIX NG display anywhere in the world. The original SieradzMeteo behavior, approved pixel-art glyphs and animations are the design baseline.

## Planned data

Weather and feels-like temperature, precipitation, snowfall, wind, clouds and pressure; European AQI, PM2.5, PM10 and seasonal pollen; sunrise/sunset, moonrise/moonset and moon phase. Agreed zero readings are suppressed, while temperature remains visible.

## Location and language

The future script will accept latitude, longitude, timezone and Polish or English labels through configurable options.

**Example only:** Sieradz, Poland — latitude `51.590748`, longitude `18.736974`, timezone `Europe/Warsaw`.

## Installation policy

An installer will only be released after confirming the supported AWTRIX NG API and testing against actual hardware. It will make a backup before changes, verify the downloaded release and support rollback. Firmware, Wi-Fi, MQTT and unrelated script settings will remain untouched.

Open-Meteo data availability varies by region and season, especially for pollen.

See the [development policy](DEVELOPMENT.md) and [main README](../README.md).


## Project illustrations

![MeteoMatrix feature overview](images/features-grid.svg)

![MeteoMatrix data flow](images/how-it-works.svg)

These illustrations show the planned features and data flow. They are not real screenshots of a released device build.


## Source and development testing

- [Preserved v1.5 original](../src/legacy/SieradzMeteo_v1_6.ax)
- [MeteoMatrix development source](../src/MeteoMatrix.ax)
- [Python installer](../tools/meteomatrix.py)
- [Development installation guide](INSTALL_EN.md)

English display labels have been added but are not hardware-verified; v1.6 astronomy animations are imported; update and rollback validation are not complete.


## Confirmed device behavior

**The original SieradzMeteo v1.6 has been verified working on a Ulanzi TC001 by the maintainer.** It is the baseline. The modified MeteoMatrix version is now maintainer-confirmed installed and working on TC001. Update and restore workflows still need separate verification.


**Milestone — 2026-11-18:** the maintainer confirms that MeteoMatrix is installed and working on TC001. This does not independently verify all settings, updates or rollback.


## Verified installation paths — 2026-11-19

The maintainer confirmed both supported installation paths working on TC001: the Python installer and the AWTRIX NG web interface. Upgrade-in-place and restore/rollback are pending separate confirmation.
