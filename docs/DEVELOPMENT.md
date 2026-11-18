# MeteoMatrix — developer guide / zasady rozwoju

## Verified milestones / Potwierdzone etapy

- [x] Public repository and Polish/English documentation.
- [x] Preserve the original SieradzMeteo v1.6 reference source and approved pixel-art.
- [x] Implement configurable latitude, longitude, IANA timezone and PL/EN labels.
- [x] Import 26 screens, Sun/Moon animations and lunar phase from v1.6.
- [x] Verify basic operation on a physical Ulanzi TC001 (maintainer report).
- [x] Verify installation through AWTRIX NG web UI (maintainer report).
- [x] Verify installation through Python tool (maintainer report).
- [x] Publish [v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/tag/v1.0.0-rc1) with a versioned `.ax` and SHA-256 checksum.
- [x] Run Python installer guardrail tests and GitHub Actions documentation checks.
- [ ] Independently test an upgrade over an existing MeteoMatrix installation.
- [ ] Independently test restoration/rollback from an earlier backup.
- [ ] Verify non-default timezones, alternate locations and both UI language selections.
- [ ] Validate Berry code through a dedicated firmware-compatible automated check (CI currently tests Python and source preservation, not Berry compilation).
- [ ] Choose and publish the intended open-source license.
- [ ] Publish the stable v1.0.0 after acceptance.

## Version lineage

- [`src/legacy/SieradzMeteo_v1_5.ax`](../src/legacy/SieradzMeteo_v1_5.ax): older historical source.
- [`src/legacy/SieradzMeteo_v1_6.ax`](../src/legacy/SieradzMeteo_v1_6.ax): **verified working reference** with original astronomy and graphics.
- [`src/MeteoMatrix.ax`](../src/MeteoMatrix.ax): universal adaptation of **v1.6**, verified running on TC001.

Legacy SieradzMeteo version numbers and MeteoMatrix release versions are independent.

## Installation and rollback rules

- Preserve the approved glyph bitmaps and event animation routines.
- Keep network coordinates, timezone and language configurable.
- Never embed credentials or private device-specific addresses in distributed code.
- Preserve unrelated scripts and device settings (firmware, Wi-Fi, MQTT).
- Installer must require `--apply` for writes, backup an existing script before modification, verify API responses and compare returned source.
- Avoid automatic rollback on an ambiguous network response; inspect device state and restore deliberately.
- Do not claim an initial installation proves safe upgrades and rollback.
- Publish release assets from a versioned tag; retain integrity checksums.
- Before a stable release, test upgrade and rollback on real hardware.

## Current release

Public pre-release: [v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/tag/v1.0.0-rc1).

[Installation guide (PL)](INSTALL_PL.md) · [Installation guide (EN)](INSTALL_EN.md)
