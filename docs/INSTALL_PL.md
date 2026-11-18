# Instalacja MeteoMatrix v1.0.0-rc1

> **Status:** [v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/tag/v1.0.0-rc1) to opublikowana wersja przedpremierowa oparta na sprawdzonym SieradzMeteo v1.6. Użytkownik potwierdził działanie aplikacji na TC001 po instalacji przez Python i panel AWTRIX NG. Aktualizacja istniejącej instalacji oraz przywracanie kopii wymagają osobnych testów.

## Wymagania

- Urządzenie z AWTRIX NG i włączonym Berry.
- Komputer z Pythonem 3.9+ i dostępem HTTP do AWTRIX NG.
- Kopia repozytorium `sp7uto/awtrix-meteomatrix`.
- Opcjonalnie login do interfejsu urządzenia; hasło podaj przez zmienną `AWTRIX_PASSWORD`, a nie jako argument polecenia.

## Tryb kontrolny (niczego nie zmienia)

W katalogu repozytorium uruchom:

```bash
python3 tools/meteomatrix.py status --host 10.0.0.11
python3 tools/meteomatrix.py install --host 10.0.0.11
```

Adres `10.0.0.11` jest **wyłącznie przykładem prywatnej instalacji**; wpisz adres własnego urządzenia.

Instalator **zawsze używa nazwy aplikacji `MeteoMatrix`**, o ile nie zmienisz jej parametrem `--name`. Nie modyfikuje aplikacji `SieradzMeteo`.

## Instalacja wydania RC1

```bash
python3 tools/meteomatrix.py install --host ADRES_TWOJEGO_AWTRIX --apply
```

Po instalacji sprawdź wyświetlanie i ustawienia skryptu (Latitude, Longitude, Timezone, Language) przez ⚙ w interfejsie AWTRIX NG. Domyślne współrzędne Sieradza są przykładem i **mogą wymagać zmiany przed użyciem**.

## Kopia bezpieczeństwa / przywracanie

```bash
python3 tools/meteomatrix.py backup --host ADRES_TWOJEGO_AWTRIX
python3 tools/meteomatrix.py restore --host ADRES_TWOJEGO_AWTRIX --file backups/NAZWA-KOPII.ax
python3 tools/meteomatrix.py restore --host ADRES_TWOJEGO_AWTRIX --file backups/NAZWA-KOPII.ax --apply
```

Przy aktualizacji istniejącego skryptu instalator zapisuje jego kod do katalogu `backups/` z sumą SHA-256 w nazwie. Aktualizuje tylko przez API `script-update`, które porównuje dokładny poprzedni kod. Nie próbuje na siłę nadpisywać niezgodnej wersji.

**W razie niejednoznacznej odpowiedzi urządzenia nie następuje automatyczny rollback**, aby nie nadpisać innych zmian. Najpierw sprawdź stan, potem użyj przywracania. Przy pierwszej instalacji problematyczny skrypt może wymagać ręcznego usunięcia w panelu urządzenia.

## Uruchomienie testów

```bash
python3 -m unittest discover -s tests -v
```

Nie dotykaj firmware, Wi-Fi ani MQTT: narzędzie do MeteoMatrix nie zmienia tych ustawień.


## Potwierdzenie metod instalacji

19.11.2026: użytkownik potwierdził prawidłową instalację przez skrypt Python oraz panel AWTRIX NG na TC001. Aktualizację istniejącego skryptu i przywracanie poprzedniej wersji należy nadal traktować jako nieprzetestowane osobno.
