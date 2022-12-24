# Weather app client

**Client for [weather_app](https://github.com/MichalUSER/weather_app) built with micropython**

## Requirements

- MicroPython compatible development board (e.g. esp32)
- Python 3.8.0 (install with [pyenv](https://github.com/pyenv/pyenv))

## Uploading your code

1. Install ampy

```
pip3 install --user adafruit-ampy
```

3. Fill out env.example.py and rename to env.py

```
ampy --port /dev/ttyUSB0 --baud 115200 put env.py
```

2. Upload code

```
ampy --port /dev/ttyUSB0 --baud 115200 put main.py
```

## Links

[weather_app](https://github.com/MichalUSER/weather_app)
— [weather_app_server](https://github.com/MichalUSER/weather_app_server)
— [weather_app_cli](https://github.com/MichalUSER/weather_app_cli)
