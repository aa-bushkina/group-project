
# Проверка совпадения количества портов с заявленным
def check(allPorts, ioPorts, groundPorts, uselessPorts):
    if len(allPorts) != 40:
        print("Недостаточное количество рабочих портов\n")
        exit(1)
    if len(ioPorts) != 26 or len(groundPorts) != 8 or len(uselessPorts) != 6:
        print("Недостаточное количество IO-портов\n")
        exit(1)