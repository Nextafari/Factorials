import requests
import json


def bitfinex():
    call = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    return call.json()

action = bitfinex()
print(action)