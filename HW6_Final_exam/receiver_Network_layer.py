import socket
import pickle
import time


def receiver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9992))
    server.listen()

    datalink, addr = server.accept()
    print('Connect Datalink layer\nHost IP:', addr[0], '\nPort:', addr[1]) 
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9994))
    print('Connect Transport layer')

    while True:
        packet = datalink.recv(1024)
        
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
    receiver()
