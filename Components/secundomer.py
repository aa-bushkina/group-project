import threading
import time

from config import event, eventForClock
from hand_detect import run_until_hand_detected
from utils import clearPorts


def secundomer(ports, timetostop):
    sec = 0
    while True:
        for i in range(0, 12):
            for j in range(0, 5):
                ports[i].lightOn()
                print(sec)
                time.sleep(0.5)
                sec += 1
                ports[i].lightOff()
                time.sleep(0.5)
                if sec == timetostop:
                    event.clear()
                    eventForClock.clear()
                    clearPorts(ports)
                    print("Конец секундомера")
                    return
                if event.isSet():
                    event.clear()
                    eventForClock.clear()
                    clearPorts(ports)
                    print("Конец секундомера")
                    return


def stopwatch(ports, timeToStop):
    threading.Timer(interval=1, function=run_until_hand_detected, args=[lambda: secundomer(ports, timeToStop)]).start()
    print("Помашите рукой если хотите остановить секундомер")