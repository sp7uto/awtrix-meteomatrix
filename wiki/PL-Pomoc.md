# Rozwiązywanie problemów

[[← Słońce i Księżyc|PL-Slonce-i-Ksiezyc]] · [[Strona główna|Home]]

## Aplikacja nie pojawia się na wyświetlaczu

Sprawdź, czy skrypt `MeteoMatrix` jest zainstalowany i uruchomiony w panelu AWTRIX NG oraz czy urządzenie ma dostęp do Internetu.

## Nieprawidłowe godziny wschodu i zachodu

Sprawdź `latitude`, `longitude` i `timezone`. Dla Polski przykładową strefą jest `Europe/Warsaw`.

## Brak niektórych parametrów

Zależnie od lokalizacji, pory roku i dostępności Open-Meteo wybrane dane (szczególnie pyłki) mogą nie być udostępniane.

## Kontrola instalacji przez Python

```bash
python3 tools/meteomatrix.py status --host ADRES_AWTRIX
```

Polecenie wyświetla stan i nie wprowadza zmian.

## Zgłaszanie problemów

Zgłoszenia przyjmujemy na stronie [GitHub Issues](https://github.com/sp7uto/awtrix-meteomatrix/issues). Dołącz wersję AWTRIX NG, wersję MeteoMatrix, opis objawów i komunikaty błędów. **Nie zamieszczaj haseł, tokenów ani prywatnych danych dostępowych.**
