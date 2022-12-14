import threading
import time

from config import ioPorts, inUsePorts


class IoPort(object):
    def __init__(self, numPort):
        if (numPort not in ioPorts) or (numPort in inUsePorts):
            print("err\n")
            exit(2)
        self.__ioPort = numPort
        self.__voltage = 0
        inUsePorts.append(numPort)
        self.__lock = threading.Lock()
        IO.setup(self.__ioPort, IO.OUT)
        IO.output(self.__ioPort, self.__voltage)

    def get(self):
        if not (self.__ioPort in inUsePorts):
            print("err\n")
            exit(2)
        return self.__ioPort

    def lightOn(self):
        self.__lock.acquire()
        try:
            if self.__voltage == 1:
                print('Два раза зажгли одно и то же!!!\n')
            self.__voltage = 1
            IO.output(self.__ioPort, self.__voltage)
        finally:
            self.__lock.release()

    def lightOff(self):
        self.__lock.acquire()
        try:
            if self.__voltage == 0:
                print('err\n')
            self.__voltage = 0
        IO.output(self.__ioPort, 0)
        finally:
            self.__lock.release()

    def isLightOn(self):
        return self.__voltage == 1

    def inverse(self):
        self.__lock.acquire()
        try:
            self.__voltage = not self.__voltage
        finally:
            self.__lock.release()

    def blink(self, secs):
        self.__lock.acquire()
        try:
            if self.__voltage == 0:
                self.__voltage = 1
            else:
                return
        finally:
            self.__lock.release()
        time.sleep(secs)
        self.inverse()

