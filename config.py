event = threading.Event()
eventForClock = threading.Event()


ioPorts = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]
groundPorts = [6, 9, 14, 20, 25, 30, 34, 39]
uselessPorts = [1, 2, 4, 17, 27, 28]
inUsePorts = []