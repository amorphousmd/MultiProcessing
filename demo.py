# Demo cach dung module client
import time

from client import *
e = [(1, 5, 0), (9, 4, 0), (2, 6, 0), (6, 7, 0)]
f = [(1, 5), (1, 1), (2, 6), (6, 1)]

# Main guard
if __name__ == '__main__':
    startClient() # Can phai bat server truoc
    # Gui du lieu
    sendData(e)
    time.sleep(1)
    sendData(zeroExtend(f))
    time.sleep(1)
    sendData(e)
    time.sleep(1)
    stopClient()  # Dong client se dong luon ca server, chi goi khi da thuc hien xong chuong trinh