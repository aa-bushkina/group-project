from config import ioPorts, groundPorts, uselessPorts, allPorts, eventForClock
from utils import *


def main():
    check(allPorts, ioPorts, groundPorts, uselessPorts)
    # IO.setmode(IO.BOARD)
    ports = []
    for i in range(0, 12):
        ports.append(IoPort(ioPorts[i]))
    if len(ports) != 12:
        print("err")
        exit(3)


if __name__ == '__main__':
    main()
