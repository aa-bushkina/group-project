import math
import datetime
import threading
import time

from config import eventForClock, event
from hand_detect import run_until_hand_detected
from utils import clearPorts


def startClock(io_ports_for_clock):
    hourNow = datetime.datetime.now().time().hour
    minuteNow = datetime.datetime.now().time().minute
    ioPorts = io_ports_for_clock
    while not eventForClock.isSet():
        temp_hours = ioPorts[hourNow % 12]
        if not ioPorts[hourNow % 12].isLightOn():
            ioPorts[hourNow % 12].lightOn()
        if hourNow % 12 != math.floor(minuteNow / 5):
            ioPorts[math.floor(minuteNow / 5)].lightOn()
        time.sleep(0.5)
        if hourNow % 12 != math.floor(minuteNow / 5):
            ioPorts[math.floor(minuteNow / 5)].lightOff()
        time.sleep(0.5)
        minuteNow = datetime.datetime.now().time().minute
        hourNow = datetime.datetime.now().time().hour
        if ioPorts[hourNow % 12].get() != temp_hours.get():
            temp_hours.lightOff()
    event.clear()
    eventForClock.clear()
    clearPorts(io_ports_for_clock)


def doClock(ports):
    threading.Timer(interval=1, function=run_until_hand_detected, args=[lambda: startClock(ports)]).start()
    print("Помашите рукой если хотите остановить часы")