import socket 
import random
import time

HOST = '127.0.0.1'
PORT = 9999

receiver_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

receiver_socket.connect((HOST, PORT)) 

m = 3
size = (m ** 2) - 1

ack = 1

while ack < size:
    receiver_socket.send(str(ack).encode())
    data = receiver_socket.recv(1024)
    packet = int(data.decode())
    if packet == ack:
        print('Received Packet: ', data.decode())
        var = random.choice([True, False])
        if var:
            print("Send ACK ", ack)
            ack += 1
        else:
            print("Lost ACK")
            time.sleep(1)
            print("Send ACK ", ack)
            ack += 1

receiver_socket.send("Final".encode())
receiver_socket.close() 