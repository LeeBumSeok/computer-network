import socket
import pickle
import time


def sender():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9997))
    server.listen()

    transport, addr = server.accept()
    print('Connect Trnasport layer\nHost IP:', addr[0], '\nPort:', addr[1]) 

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9996))
    print('Connect Datalink layer') 

    while True:
        packet = transport.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break

        print("message: " + str(data[0]) + ", Packet: " + str(data[1]))
        time.sleep(1)
        client.send(packet)

if __name__ == '__main__':
    sender()
