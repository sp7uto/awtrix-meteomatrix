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
- [ ] Verified source import
- [ ] Generic configuration and translated labels
- [ ] Automated validation for the real Berry source
- [ ] API-compatible backup and installer
- [ ] On-device testing and rollback validation
- [ ] First release candidate
- [ ] Stable release and optional AWTRIX Hub listing

Historical SieradzMeteo version numbers are not MeteoMatrix release numbers.
