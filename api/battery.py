from flask import request
from datetime import datetime

import random

battery = {

}

response = "hello"

def search() -> list:
    return battery

def addnew():
    hash = random.getrandbits(64)
    print (hash)
    batt = { hash : {
        "batlife": request.json['batlife'],
        "charging": request.json['charging'],
        "time": datetime.now(),
        "timeleft": request.json['timeleft']
        }
    }
    battery.update(batt)
    return batt
