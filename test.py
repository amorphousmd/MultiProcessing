# Example of using a pipe between processes
import time
from multiprocessing import Process
from multiprocessing import Pipe
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
e = [(1, 5, 0), (9, 4, 0), (2, 6, 0), (6, 7, 0)]
f = [(1, 5), (4, 22), (2, 0), (6, 7)]

def getvalue():
    print(sendDataOrder)

def createData(coords_list):
    list1 = [elem for coords in coords_list for elem in coords]
    msg = ""
    for i in list1:
        msg += ","
        msg += str(i)
    msg = str(len(coords_list)) + msg
    return msg


def function():
    global sendDataOrder
    sendDataOrder = True


def sendCoordinates(inputCoords):
    if connected:
        global dataBuffer
        dataBuffer = createData(inputCoords)
    else:
        print("Socket not connected")


def closeClient():
    global closeClientOrder
    closeClientOrder = True

# generate work
def sender(connection, data):
    print('Sender: Running', flush=True)
    connection.send(data)
    # all done
    print('Sender: Done', flush=True)


# consume work
def receiver(connection):
    # HOST = '192.168.1.1'
    HOST = '127.0.0.1'
    PORT = 5050
    server_address = (HOST, PORT)
    print(f'[CONNECTING] TO PORT: {server_address}')
    clientSocket.connect(server_address)
    while True:
        data = connection.recv()
        clientSocket.sendall(bytes(data, "utf8"))


# entry point
if __name__ == '__main__':
    conn1, conn2 = Pipe(duplex=True)
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    sender_process = Process(target=sender, args=(conn2, createData(e)))
    sender_process.start()
    time.sleep(1)
    sender_process = Process(target=sender, args=(conn2, createData(f)))
    sender_process.start()

