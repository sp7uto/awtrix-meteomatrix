# Changelog / Historia zmian

## Unreleased — initial repository scaffold
- Initialized `sp7uto/awtrix-meteomatrix`.
- Added bilingual project and developer documentation.
- Defined portable location settings, approved animation preservation and safe-update requirements.
- No installable Berry file is released yet.

## Development scaffold — 2026-11-18
- Imported exact available SieradzMeteo v1.5 Berry source to `src/legacy/`.
- Added preliminary `src/MeteoMatrix.ax` with latitude, longitude and timezone settings, preserving glyph bitmaps.
- Added Python backup-first development installer with explicit write opt-in and conditional update API.
- Added safety tests, GitHub Actions checks, and bilingual installation guides.
- Physical TC001 validation, PL/EN labels require hardware testing; v1.6 sun/moon animations remain pending.

- Added a development PL/EN label selector to MeteoMatrix; preserved existing glyph bitmaps.
- Changed new script installation to atomic compare-and-swap to avoid overwriting concurrent changes.
