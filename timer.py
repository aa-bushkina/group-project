import threading
import time

from config import event, eventForClock
from hand_detect import run_until_hand_detected
from utils import debugShow, clearPorts


def timer(ports, start_minutes, start_seconds):
    if type(start_minutes) != int or type(start_seconds) != int:
        print("НЕКОРРЕКТНОЕ ЧИСЛО")
        return
    if start_minutes < 0 or start_minutes > 11:
        print("НЕКОРРЕКТНОЕ КОЛИЧЕСТВО МИНУТ")
        return
    if start_seconds < 0 or start_seconds > 59:
        print("НЕКОРРЕКТНОЕ КОЛИЧЕСТВО СЕКУНД")
        return
    is_first_iteration = True
    is_equals = False
    minutes_port = start_minutes
    sec_port = start_seconds // 5
    while minutes_port >= 0:  # Цикл по всему времени
        if minutes_port != 0:
            ports[minutes_port].lightOn()
        while sec_port >= 0:  # Цикл по секундам в рамках одной минуты
            sec = 0
            sec_delta = 5
            if is_first_iteration:
                sec_delta = start_seconds - (start_seconds // 5) * 5
                is_first_iteration = False

            if sec_port == minutes_port and minutes_port != 0:
                num_iter = 0
                while sec < sec_delta:  # Цикл по 5 секундам (мигание одной лампочки), когда минуты совпали с секундами
                    if num_iter != 0:
                        ports[sec_port].lightOn()
                    num_iter = num_iter + 1
                    is_equals = True
                    #debugShow(ports)
                    time.sleep(0.3)
                    ports[sec_port].lightOff()
                    time.sleep(0.7)
                    sec = sec + 1
            else:
                while sec < sec_delta:  # Цикл по 5 секундам (мигание одной лампочки)
                    ports[sec_port].lightOn()
                    #debugShow(ports)
                    time.sleep(0.3)
                    ports[sec_port].lightOff()
                    time.sleep(0.7)
                    sec = sec + 1
            sec_port = sec_port - 1
            if is_equals:
                ports[minutes_port].lightOn()
                is_equals = False
        sec_port = 11
        if minutes_port != 0:
            ports[minutes_port].lightOff()
        minutes_port = minutes_port - 1

    print("Помашите рукой")

    threading.Timer(interval=1, function=run_until_hand_detected, args=[lambda: endOfTimer(ports)]).start()


def endOfTimer(ports):
    blink_interval = 0.3
    delay_next = 0.1
    while not event.isSet():
        for port in ports:
            threading.Thread(target=port.blink, args=[blink_interval]).start()
            time.sleep(delay_next)
    event.clear()
    eventForClock.clear()
    clearPorts(ports)
    print("Конец таймера")