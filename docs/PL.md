![MeteoMatrix — baner projektu dla AWTRIX NG](images/hero-meteomatrix.png)

# MeteoMatrix — dokumentacja polska

## Stan projektu

**Opublikowano [MeteoMatrix v1.0.0-rc1](https://github.com/sp7uto/awtrix-meteomatrix/releases/tag/v1.0.0-rc1).** Jest to pierwsze publiczne wydanie przedpremierowe (Release Candidate), oparte na sprawdzonym **SieradzMeteo v1.6**.

Użytkownik potwierdził poprawne działanie MeteoMatrix na **Ulanzi TC001 / AWTRIX NG** po instalacji **obiema metodami**: przez instalator Python oraz panel WWW AWTRIX NG. Oddzielnego sprawdzenia wymagają aktualizacja zainstalowanej wersji i przywracanie poprzedniej wersji (rollback).

**[Pobierz MeteoMatrix.ax](https://github.com/sp7uto/awtrix-meteomatrix/releases/download/v1.0.0-rc1/MeteoMatrix.ax)** · **[Suma SHA-256](https://github.com/sp7uto/awtrix-meteomatrix/releases/download/v1.0.0-rc1/MeteoMatrix.ax.sha256)** · **[Opis wydania PL/EN](../release/notes-v1.0.0-rc1.md)**

## Funkcje

- 26 ekranów pogodowych i środowiskowych.
- Temperatura rzeczywista i odczuwalna, opady, śnieg, wiatr, zachmurzenie i ciśnienie.
- European AQI, PM2.5, PM10 oraz pyłki roślin w sezonie.
- Wschody i zachody Słońca i Księżyca, faza Księżyca.
- Oryginalne ikony pikselowe 8×8 i animacje z SieradzMeteo v1.6.
- Ukrywanie określonych wskazań zerowych, z zachowaniem prezentacji temperatury.
- Konfiguracja lokalizacji, strefy czasowej i etykiet PL/EN.

## Ustawienia

| Parametr | Przykładowa wartość |
| --- | --- |
| Szerokość geograficzna | `51.590748` |
| Długość geograficzna | `18.736974` |
| Strefa czasowa | `Europe/Warsaw` |
| Język | `pl` albo `en` |

Wartości dotyczą Sieradza i są wyłącznie ustawieniami domyślnymi. Konfiguracja odbywa się przez ustawienia aplikacji Berry w AWTRIX NG.

## Instalacja i bezpieczeństwo

Obie metody instalacji zostały potwierdzone przez użytkownika:
1. Bezpośrednie wgranie pliku `.ax` w panelu AWTRIX NG.
2. Instalator Python z repozytorium.

Szczegóły: **[Instrukcja instalacji PL](INSTALL_PL.md)**. Instalator ma tryb kontrolny bez zapisu, wymaga jawnego `--apply`, zachowuje kopię przy aktualizacji istniejącego skryptu i obsługuje ręczne przywrócenie. **Aktualizacja istniejącej aplikacji i rollback nie zostały jeszcze osobno zweryfikowane na urządzeniu.**

Nie zmieniamy firmware, konfiguracji Wi-Fi, MQTT ani innych aplikacji.

## Kod źródłowy

- [MeteoMatrix — skrypt Berry](../src/MeteoMatrix.ax)
- [Działający pierwowzór SieradzMeteo v1.6](../src/legacy/SieradzMeteo_v1_6.ax)
- [Instalator Python](../tools/meteomatrix.py)
- [Zasady rozwoju](DEVELOPMENT.md)

## Ilustracje

![Przegląd funkcji](images/features-grid.svg)

![Schemat działania — Open-Meteo → Berry → AWTRIX NG](images/how-it-works.svg)

Grafiki przedstawiają koncepcję funkcji i architektury, a nie zrzuty ekranu z urządzenia. Dostępność pyłków z Open-Meteo zależy od lokalizacji i sezonu.

[Repozytorium główne](../README.md) · [English documentation](EN.md)
