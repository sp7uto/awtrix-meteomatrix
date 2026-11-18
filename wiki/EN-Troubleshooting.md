# Troubleshooting

[[← Sun and Moon|EN-Sun-and-Moon]] · [[Home|Home]]

## App does not appear

Check that the `MeteoMatrix` Berry script is installed and enabled in AWTRIX NG, and that the device has internet access.

## Sunrise or moonrise times are wrong

Verify your `latitude`, `longitude` and `timezone`. Use an IANA timezone such as `Europe/Warsaw`.

## Some measurements are missing

Coverage varies with location, season and the availability of Open-Meteo data, especially for pollen.

## Read-only status check

```bash
python3 tools/meteomatrix.py status --host YOUR_AWTRIX_IP
```

## Report a problem

Open a [GitHub issue](https://github.com/sp7uto/awtrix-meteomatrix/issues), stating MeteoMatrix and AWTRIX NG versions, symptoms and relevant error messages. Do not disclose passwords, access tokens or private credentials.
