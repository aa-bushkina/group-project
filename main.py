from config import ioPorts, groundPorts, uselessPorts, allPorts, eventForClock
from utils import *

INFO = "Программа часы:\n" \
       "help - вывести информацию о функциях программы\n" \
       "exit - завершить программу\n" \
       "alarm day hour:minute - поставить будильник на соответствующее время\n" \
       "Например 21 08:20 -> будильник поставлен на 21 число время 8 часов 20 минут\n" \
       "sw - время через которое секундомер отключится\n" \
       "timer minutes:seconds - таймер на указанное время\n" \
       "clock - просто режим работы часов"  # TODO  дописать доку для своих функций


def main():
    check(allPorts, ioPorts, groundPorts, uselessPorts)
    # IO.setmode(IO.BOARD)
    ports = []
    for i in range(0, 12):
        ports.append(IoPort(ioPorts[i]))
    if len(ports) != 12:
        print("err")
        exit(3)

    print(INFO)
    threading.Thread(target=debugInRealTime, args=[ports]).start() # FIXME Раскомментить чтобы видеть статус циферблата в реалтайме
    while True:
        raw_input = input()  # читаем команды в формате "команда аргументы"
        parse_input = raw_input.partition(' ')
        func = parse_input[0]
        args = parse_input[2]
        if func not in {"help", "exit", "sw", "alarm", "timer", "clock"}:
            print("Неправильные аргументы")
            print(INFO)
            continue
        if func == "help":
            print(INFO)
        if func == "exit":
            exit(0)
        if func == "alarm":
            setUpAlarm(ports, args)
        if func == "timer":
            timer(ports, int(args[0]), int(args[2] + args[3]))
        if func == "clock":
            doClock(ports)
        if func == "sw":
            stopwatch(ports, int(args))
    return 0


if __name__ == '__main__':
    main()
