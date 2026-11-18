# MeteoMatrix v1.0.0-rc1 — Release Candidate

## English

First public release candidate of **MeteoMatrix** for **AWTRIX NG / Ulanzi TC001 (32×8)**.

**Included**
- 26 weather and environment screens based on the previously verified SieradzMeteo v1.6.
- Original approved 8×8 pixel-art icons and animated Sun/Moon rise/set displays; moon phase.
- Open-Meteo weather, European AQI, PM2.5/PM10 and seasonal pollen.
- Configurable latitude, longitude, timezone and Polish/English labels.
- Installation using the AWTRIX NG web UI or the included Python installer.
- Python backup-first installer, SHA-256 checks and explicit restoration command.

**Verification:** The maintainer confirms installation and successful operation on a real TC001 by **both** the Python installer and web UI. CI tests have also passed.

**Release candidate limitations:** Upgrade-in-place and rollback still need dedicated real-device testing. Language and geographic edge cases may require further validation. No automatic upgrade is performed.

**Install:** Download `MeteoMatrix.ax` below and install it via AWTRIX NG script management, or consult [English installation instructions](https://github.com/sp7uto/awtrix-meteomatrix/blob/main/docs/INSTALL_EN.md). Preserve a backup of any existing script. This is a pre-release.

## Polski

Pierwsza publiczna wersja testowa **MeteoMatrix** dla **AWTRIX NG / Ulanzi TC001 (32×8)**.

**Zawartość**
- 26 ekranów pogodowych i środowiskowych na podstawie sprawdzonego SieradzMeteo v1.6.
- Oryginalne ikony pikselowe 8×8, animacje wschodów i zachodów Słońca i Księżyca oraz fazy Księżyca.
- Pogoda Open-Meteo, europejski indeks jakości powietrza, PM2.5/PM10 i pyłki sezonowe.
- Konfigurowalne współrzędne, strefa czasowa, etykiety polskie i angielskie.
- Instalacja z panelu AWTRIX NG lub instalatorem Python.
- Kopia kodu przed aktualizacją, kontrola SHA-256 i polecenie ręcznego przywrócenia kopii.

**Potwierdzenie:** autor sprawdził działanie na rzeczywistym TC001 po instalacji obiema metodami. Testy CI zaliczone.

**Ograniczenia RC:** aktualizacja istniejącej wersji i rollback nie zostały jeszcze osobno sprawdzone na urządzeniu. Wymagają także sprawdzenia nietypowe lokalizacje i ustawienia językowe. Nie jest wykonywana automatyczna aktualizacja.

**Instalacja:** pobierz poniżej `MeteoMatrix.ax` i wgraj przez panel AWTRIX NG albo skorzystaj z [instrukcji PL](https://github.com/sp7uto/awtrix-meteomatrix/blob/main/docs/INSTALL_PL.md). Wcześniej zachowaj kopię istniejącego skryptu.

SHA-256: see attached `MeteoMatrix.ax.sha256`.
