import socket
import pickle
import time


def bitStuffing(frame):
    count = 0
    sequence = ""

    for i in range(0, len(frame)):
        sequence += frame[i]
        if frame[i] == '1':
            count += 1
        else:
            count = 0
        
        if count == 5:
            sequence += 0
            count = 0

    return sequence


def sender():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9996))
    server.listen()

    network, addr = server.accept()
    print('Connect Network layer\nHost IP:', addr[0], '\nPort:', addr[1]) 

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9998))
    print('Connect Physical layer') 

    while True:
        packet = network.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break

        print("message: " + str(data[0]) + ", Packet: " + str(data[1]))

        stuffing = bitStuffing(data[0])

        print("Bit-stuffing Data : " + stuffing + ", Packet: " + str(data[1]))
        time.sleep(1)
        message = [str(stuffing), str(data[1])]
        data = pickle.dumps(message)
        client.send(data)

if __name__ == '__main__':
    sender()
