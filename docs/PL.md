![MeteoMatrix — grafika tytułowa projektu dla AWTRIX NG](images/hero-meteomatrix.png)

# MeteoMatrix — dokumentacja polska

## Stan projektu

Projekt znajduje się na etapie przygotowawczym. **Dostępna jest robocza adaptacja `.ax` oparta na v1.5, ale została potwierdzona jako działająca na TC001, jednak nie jest jeszcze wersją stabilną.** Nie zastępuj nim aktualnie działającego SieradzMeteo.

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


## Ilustracje projektu

![Przegląd funkcji MeteoMatrix](images/features-grid.svg)

**Funkcje w skrócie:** pogoda, temperatura, jakość powietrza, pyłki, Słońce i Księżyc, własna lokalizacja.

![Schemat działania MeteoMatrix](images/how-it-works.svg)

**Schemat:** Open-Meteo → skrypt Berry → wyświetlacz AWTRIX NG. Są to ilustracje funkcji planowanej aplikacji, a nie zrzuty ekranów gotowego wydania.


## Kod i instrukcja rozwojowa

- [Historyczny oryginał SieradzMeteo v1.6](../src/legacy/SieradzMeteo_v1_6.ax)
- [Roboczy skrypt MeteoMatrix](../src/MeteoMatrix.ax) — konfiguracja szerokości i długości geograficznej oraz strefy czasowej
- [Instalator Python](../tools/meteomatrix.py)
- [Instrukcja instalacji testowej](INSTALL_PL.md)

Etapy **jeszcze niezrealizowane**: testy tłumaczenia etykiet PL/EN na urządzeniu, grafiki astronomiczne v1.6 (zaimportowane, do weryfikacji), testy na urządzeniu i stabilne wydanie.


## Potwierdzenie działania

**Oryginalny SieradzMeteo v1.6 został sprawdzony na urządzeniu Ulanzi TC001 i działa.** Jest naszą bazą referencyjną. Zmieniony MeteoMatrix został zainstalowany na TC001 i użytkownik potwierdził jego prawidłowe działanie. Instalator aktualizacji i przywracania wymagają osobnej weryfikacji.


**Kamień milowy — 18.11.2026:** użytkownik potwierdził poprawne działanie zainstalowanego MeteoMatrix na TC001. Nie jest to jeszcze test wszystkich ustawień ani mechanizmu aktualizacji/przywracania.


## Potwierdzone metody instalacji — 19.11.2026

Użytkownik potwierdził działanie obu metod: instalatora Python oraz bezpośredniego wgrywania przez interfejs AWTRIX NG na TC001. Potwierdzenie dotyczy instalacji i uruchomienia aplikacji. Aktualizacja istniejącej wersji i przywracanie kopii pozostają osobnymi testami.
