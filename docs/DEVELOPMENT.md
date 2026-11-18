# Maintainer guide / Zasady rozwoju

## Rules / Zasady

1. Import the **actual working** SieradzMeteo Berry source before claiming an installable version exists. / Przed pierwszym wydaniem należy pozyskać dokładny działający kod.
2. Keep approved pixel-art and animations byte-for-byte where feasible; do not substitute recreated art. / Zachować zatwierdzone ikony i animacje.
3. Do not embed private IP addresses, authentication tokens or credentials. / Nie umieszczać prywatnych adresów ani sekretów.
4. Make latitude, longitude, timezone and language configurable. / Udostępnić ustawienia lokalizacji i języka.
5. Validate AWTRIX NG Berry settings syntax and the device update API against the target firmware. / Zweryfikować API i składnię ustawień.
6. Perform backup and integrity verification **before** installation. / Wykonać kopię i weryfikację sum przed zmianami.
7. Test a rollback on real hardware before stable release. / Przetestować przywrócenie starej wersji.
8. Never modify firmware, Wi-Fi, MQTT or unrelated apps as part of MeteoMatrix updates. / Nie zmieniać pozostałej konfiguracji urządzenia.
9. Ship stable artifacts from version tags, not unreviewed main branch. / Publikować wydania z tagów.
10. Choose an open-source license before the first reusable public release. / Wybrać licencję przed wydaniem.

## Milestones

- [x] Public repository and bilingual documentation
- [x] Import verified SieradzMeteo v1.6 source (v1.6 recovered and preserved)
- [ ] Generic configuration and translated labels (coordinates/timezone and PL/EN labels implemented; device verification pending)
- [ ] Automated validation for the real Berry source
- [x] Initial API-based backup / conditional-update installer (hardware verification pending)
- [ ] On-device testing and rollback validation
- [ ] First release candidate
- [ ] Stable release and optional AWTRIX Hub listing

Historical SieradzMeteo version numbers are not MeteoMatrix release numbers.


## Current implementation

The historical v1.5 `.ax` file is preserved unchanged in `src/legacy/`. The development `src/MeteoMatrix.ax` adds `@config` for coordinates and timezone with bitmap content preserved. PL/EN language selection is present but not hardware-verified; v1.6 Moon animations are now present; hardware validation remains outstanding. The installer has command-line read-only mode, explicit `--apply`, backup-before-update, conditional API update and source read-back checks. On ambiguous failures it does not attempt a potentially destructive automatic rollback; use explicit restore after inspection.
