import time

# Проверка совпадения количества портов с заявленным
def check(allPorts, ioPorts, groundPorts, uselessPorts):
    if len(allPorts) != 40:
        print("Недостаточное количество рабочих портов\n")
        exit(1)
    if len(ioPorts) != 26 or len(groundPorts) != 8 or len(uselessPorts) != 6:
        print("Недостаточное количество IO-портов\n")
        exit(1)

def clearPorts(ports):
    for i in range(0, 12):
        ports[i].lightOff()

def outForDebug(boolean):
    if boolean:
        print(1, end=' ')
    else:
        print(0, end=' ')

def debugShow(debugPorts):
    if len(debugPorts) != 12:
        print('Чето тут не так переделывай')
        exit(4)
    for i in range(0, 7):
        for j in range(0, 7):
            if i == 0 and j == 3:
                outForDebug(debugPorts[0].isLightOn())
            elif i == 1 and j == 4:
                outForDebug(debugPorts[1].isLightOn())
            elif i == 2 and j == 5:
                outForDebug(debugPorts[2].isLightOn())
            elif i == 3 and j == 6:
                outForDebug(debugPorts[3].isLightOn())
            elif i == 4 and j == 5:
                outForDebug(debugPorts[4].isLightOn())
            elif i == 5 and j == 4:
                outForDebug(debugPorts[5].isLightOn())
            elif i == 6 and j == 3:
                outForDebug(debugPorts[6].isLightOn())
            elif i == 5 and j == 2:
                outForDebug(debugPorts[7].isLightOn())
            elif i == 4 and j == 1:
                outForDebug(debugPorts[8].isLightOn())
            elif i == 3 and j == 0:
                outForDebug(debugPorts[9].isLightOn())
            elif i == 2 and j == 1:
                outForDebug(debugPorts[10].isLightOn())
            elif i == 1 and j == 2:
                outForDebug(debugPorts[11].isLightOn())
            else:
                print(' ', end=' ')
        print()

def debugInRealTime(ports):
    while True:
        debugShow(ports)
        time.sleep(0.4)