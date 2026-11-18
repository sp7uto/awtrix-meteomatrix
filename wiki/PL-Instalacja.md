# Instalacja MeteoMatrix

[[← Wprowadzenie|PL-Wprowadzenie]] · [[Konfiguracja →|PL-Konfiguracja]]

## Wymagania

- Ulanzi TC001 z firmware AWTRIX NG i obsługą Berry.
- Dostęp do panelu WWW AWTRIX NG.
- Plik aplikacji `MeteoMatrix.ax` z wydania projektu.

## Metoda 1 — panel AWTRIX NG

1. Pobierz [MeteoMatrix.ax — v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/download/v1.0.0-rc1/MeteoMatrix.ax).
2. Otwórz panel WWW swojego urządzenia AWTRIX NG.
3. Przejdź do zarządzania skryptami Berry i wgraj `MeteoMatrix.ax`.
4. Uruchom aplikację i ustaw lokalizację, strefę czasową oraz język.

## Metoda 2 — instalator Python

Instalator wymaga **Python 3.9+** i kopii repozytorium. Polecenia uruchom w katalogu projektu:

```bash
python3 tools/meteomatrix.py status --host ADRES_AWTRIX
python3 tools/meteomatrix.py install --host ADRES_AWTRIX
```

Powyższe polecenia nie zapisują zmian. Instalacja wymaga jawnej zgody:

```bash
python3 tools/meteomatrix.py install --host ADRES_AWTRIX --apply
```

Podmień `ADRES_AWTRIX` na adres swojego urządzenia.

**Uwaga:** instalację obiema metodami sprawdzono na TC001. Aktualizacja istniejącej wersji i odtwarzanie kopii zapasowej wymagają osobnych testów na urządzeniu.

Szczegółowa [instrukcja techniczna](https://github.com/sp7uto/awtrix-meteomatrix/blob/main/docs/INSTALL_PL.md).
