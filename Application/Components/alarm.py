import datetime
import threading
import time

from config import event, eventForClock
from hand_detect import run_until_hand_detected
from utils import clearPorts


def setUpAlarm(ports, alarm_time_raw):
    if isinstance(alarm_time_raw, str):
        alarm_time_parsed = datetime.datetime.strptime(alarm_time_raw, '%d %H:%M')
        # Передаём только день и время, остальные параметры берём из текущего времени
        alarm_time = datetime.datetime.now().replace(day=alarm_time_parsed.day, hour=alarm_time_parsed.hour,
                                                     minute=alarm_time_parsed.minute)
    else:
        alarm_time = alarm_time_raw
    delay = alarm_time - datetime.datetime.now()
    if delay.total_seconds() < 0:
        print(f"Будильник: неправильно передано время {alarm_time_parsed}")
        return
    print(f"Будильник: успешно установлен на время {alarm_time}. Зазвонит через {delay.total_seconds()} сек")
    # threading.Thread().start() #FIXME пример запуска вашей функции с выключением по взмаху руки
    threading.Timer(interval=delay.total_seconds(), function=run_until_hand_detected,
                    args=[lambda: alarm(ports)]).start()


def alarm(ports):
    blink_interval = 0.3
    delay_next = 0.1
    while not event.isSet():
        for port in ports:
            threading.Thread(target=port.blink, args=[blink_interval]).start()
            time.sleep(delay_next)
    event.clear()
    eventForClock.clear()
    clearPorts(ports)
    print("Замечена рука, функция остановилась")
