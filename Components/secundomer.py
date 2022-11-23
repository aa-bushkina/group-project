import threading
import time

from config import event, eventForClock
from hand_detect import run_until_hand_detected
from utils import debugShow, clearPorts


def secundomer(ports, timetostop):
    sec = 0
    while True:
        for i in range(0, 12):
            for j in range(0, 5):
                ports[i].lightOn()
                debugShow(ports)
                time.sleep(0.5)
                sec += 1
                ports[i].lightOff()
                time.sleep(0.5)
                debugShow(ports)
                if sec == timetostop:
                    event.clear()
                    eventForClock.clear()
                    clearPorts(ports)
                    return
                if event.isSet():
                    event.clear()
                    eventForClock.clear()
                    clearPorts(ports)
                    return