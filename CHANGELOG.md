# Changelog / Historia zmian

## Unreleased — initial repository scaffold
- Initialized `sp7uto/awtrix-meteomatrix`.
- Added bilingual project and developer documentation.
- Defined portable location settings, approved animation preservation and safe-update requirements.
- Initially no Berry file was released; the first public pre-release is v1.0.0-rc1.

## Development scaffold — 2026-11-18
- Imported exact available SieradzMeteo v1.6 Berry source to `src/legacy/`.
- Added preliminary `src/MeteoMatrix.ax` with latitude, longitude and timezone settings, preserving glyph bitmaps.
- Added Python backup-first development installer with explicit write opt-in and conditional update API.
- Added safety tests, GitHub Actions checks, and bilingual installation guides.
- Physical TC001 validation, PL/EN labels require hardware testing; v1.6 sun/moon animations imported; hardware verification pending.

- Added a development PL/EN label selector to MeteoMatrix; preserved existing glyph bitmaps.
- Changed new script installation to atomic compare-and-swap to avoid overwriting concurrent changes.

## Development update — 2026-11-18 (v1.6 recovery)
- Recovered original 520-line SieradzMeteo v1.6 from Library and preserved it under `src/legacy/`.
- Rebased MeteoMatrix on v1.6 while retaining 26-page layout, original bitmap artwork, Sun/Moon animated events and lunar phase.
- Updated pixel-art preservation tests to compare against v1.6.
- Update and rollback testing remains pending; no stable release is published.

- Recorded maintainer confirmation that the recovered original SieradzMeteo v1.6 works on a physical TC001; the universal MeteoMatrix adaptation still needs separate verification.

- 2026-11-18: Maintainer confirmed universal MeteoMatrix installed and functioning on Ulanzi TC001; release, update and restore qualification remain separate.

- 2026-11-19: Maintainer confirmed successful TC001 installation by both the Python installer and the AWTRIX NG web UI; upgrade and rollback checks remain outstanding.


## v1.0.0-rc1 — public prerelease
- Published tagged GitHub prerelease with MeteoMatrix.ax and SHA-256 checksum.
- Ran automated checks in the publishing workflow.
- Installation confirmed on TC001 via Python tool and AWTRIX NG web panel.
- Upgrade/rollback verification remains open.
