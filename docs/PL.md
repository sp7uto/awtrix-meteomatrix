# MeteoMatrix — dokumentacja polska

## Stan projektu

Projekt znajduje się na etapie przygotowawczym. **Nie ma jeszcze kompletnego, przetestowanego pliku `.ax` do instalacji.** Nie zastępuj nim aktualnie działającego SieradzMeteo.

## Przeznaczenie

MeteoMatrix to uniwersalny skrypt pogodowy dla AWTRIX NG / Ulanzi TC001. Użytkownik wybierze lokalizację, strefę czasową i język. Obecna konfiguracja Sieradza służy jako wzorzec zachowania i grafiki.

## Planowane funkcje

- Temperatura rzeczywista i odczuwalna, opady, śnieg, wiatr, zachmurzenie oraz ciśnienie.
- Jakość powietrza: European AQI, PM2.5 i PM10, a także pyłki roślin w sezonie.
- Wschody i zachody Słońca oraz Księżyca i aktualna faza Księżyca.
- Oryginalne, wcześniej zatwierdzone grafiki pikselowe i animacje.
- Ukrywanie wybranych parametrów o wartości zerowej, z wyjątkiem temperatury.
- Ustawienia lokalizacji i języka PL/EN bez edycji kodu.

## Przykładowa lokalizacja

| Ustawienie | Przykład |
| --- | --- |
| Miasto | Sieradz |
| Latitude | `51.590748` |
| Longitude | `18.736974` |
| Timezone | `Europe/Warsaw` |
| Language | `pl` |

To **przykład**, a nie ustawienia wszystkich instalacji.

## Instalacja i aktualizacje

Instalator zostanie udostępniony po potwierdzeniu działania API konkretnej wersji AWTRIX NG. Jego zadania obejmą wykonanie kopii skryptu na urządzeniu, weryfikację pobranej wersji, kontrolę błędów i przywrócenie poprzedniej wersji w razie niepowodzenia.

Nie będzie modyfikował firmware, ustawień Wi-Fi, MQTT ani innych aplikacji.

## Użyte źródła

Dane pogodowe pochodzą z Open-Meteo. Dostępność danych o pyłkach zależy od obszaru i sezonu.

Zobacz też [zasady rozwoju](DEVELOPMENT.md) oraz [README](../README.md).
