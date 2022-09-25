import time

from client import *
e = [(1, 5, 0), (9, 4, 0), (2, 6, 0), (6, 7, 0)]

if __name__ == '__main__':
    startClient()
    sendData(e)
    time.sleep(1)
    sendData(e)
    time.sleep(1)
    sendData(e)
    time.sleep(1)
    stopClient()
