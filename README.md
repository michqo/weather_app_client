# Weather app client

**Client for [weather_app](https://github.com/MichalUSER/weather_app) built with micropython**

## Requirements

- ESP32 development board
- Python 3.8.0 (install with [pyenv](https://github.com/pyenv/pyenv))

## Uploading your code

1. Install ampy

```bash
pip3 install --user adafruit-ampy
```

3. Fill out env.py

Follow env.example.py to set your own secret variables.

2. Upload code

```bash
ampy --port /dev/ttyUSB0 --baud 115200 put main.py
```

## Links

[weather_app](https://github.com/MichalUSER/weather_app)
— [weather_app_server](https://github.com/MichalUSER/weather_app_server)
— [weather_app_cli](https://github.com/MichalUSER/weather_app_cli)
