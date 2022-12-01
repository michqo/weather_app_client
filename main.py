from machine import Timer
from machine import Pin
from time import sleep
import machine
import dht
import network
import urequests as requests
import ujson
from env import SSID, PASS, SECRET, LOG

sleep(2)

URL = "https://weather-uno.fly.dev"
address = f"{URL}/add_temp2/{SECRET}"
address2 = f"{URL}/add_last_temp/{SECRET}"

tim0 = Timer(0)
tim1 = Timer(1)

sensor = dht.DHT22(Pin(15))

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID, PASS)
        while not wlan.isconnected():
            machine.idle()

def log(msg):
    f = open("log.txt", "a")
    f.write(f"{msg}\n")
    f.close()

if LOG:
    log("started")

tries = 1
def measure():
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        # For when sensor measures incorrectly
        if temp == -50.0:
            if LOG:
                log("Temp is -50")
            sleep(60)
            return measure()
        data = {
            "averageTemp": f"{temp:.1f}",
            "humidity": f"{humidity:.1f}",
        }
        return data
    except OSError:
        if LOG:
            log(f"Error occured in measure()")
        global tries
        if tries >= 2:
            tries = 1
            return "{}"
        sleep(tries * 30)
        tries += 1
        return measure()

tries2 = 1
def post_temp():
    try:
        data = ujson.dumps(measure())
        res = requests.post(address, headers = {'content-type': 'application/json'}, data = data).json()
        if LOG:
            log(res)
    except:
        if LOG:
            log(f"Error occured in hour()")
        global tries2
        if tries2 > 2:
            tries2 = 1
            return
        sleep(tries2 * 60)
        tries2 += 1
        post_temp()

def last():
    try:
        data = ujson.dumps(measure())
        requests.post(address2, headers = {'content-type': 'application/json'}, data = data).json()
    except:
        pass

def hour():
    tim1.deinit()
    connect_wifi()
    post_temp()
    tim1.init(period=(int(1000 * 60 * 10.3)), mode=Timer.PERIODIC, callback=lambda _:last())

hour()

tim0.init(period=(1000 * 60 * 60), mode=Timer.PERIODIC, callback=lambda _:hour())
