import datetime
import threading
import time

from config import event, eventForClock
from hand_detect import run_until_hand_detected
from utils import clearPorts

def alarm(ports):
    blink_interval = 1
    delay_next = 1
    while not event.isSet():
        for port in ports:
            threading.Thread(target=port.blink, args=[blink_interval]).start()
            time.sleep(delay_next)
    event.clear()
    eventForClock.clear()
    clearPorts(ports)
