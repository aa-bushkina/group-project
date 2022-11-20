from config import ioPorts, inUsePorts


class IoPort(object):
    def __init__(self, numPort):
        if (numPort not in ioPorts) or (numPort in inUsePorts):
            print("err")
            exit(2)
        self.__ioPort = numPort
        self.__voltage = 0
        inUsePorts.append(numPort)
        self.__lock = threading.Lock()
        # IO.setup(self.__ioPort, IO.OUT)
        # IO.output(self.__ioPort, self.__voltage)

    def get(self):
        if not (self.__ioPort in inUsePorts):
            print("err")
            exit(2)
        return self.__ioPort

    def lightOn(self):
        self.__lock.acquire()
        try:
            if self.__voltage == 1:
                print('Два раза зажгли одно и то же!!!\n')
            self.__voltage = 1
            # IO.output(self.__ioPort, self.__voltage)
        finally:
            self.__lock.release()

    def lightOff(self):
        self.__lock.acquire()
        try:
            if self.__voltage == 0:
                print('Два раза выключили одно и то же!!!\n')
            self.__voltage = 0
        # IO.output(self.__ioPort, 0)
        finally:
            self.__lock.release()

    def isLightOn(self):
        return self.__voltage == 1
