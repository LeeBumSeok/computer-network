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

window = list()
count = 0
while ack < size:
    for i in range(0, m + 1):
        window.append(i)
    print("---------------------------------------")
    receiver_socket.send(str(window[count]).encode())
    count += 1
    if count > 3:
        count = 0
    data = receiver_socket.recv(1024)
    packet = int(data.decode())
    print('Received Packet: ', data.decode())
    var = random.choice([True, False])
    if var:
        print("Send ACK ", window[count])
        ack += 1
    else:
        print("Lost ACK")
        time.sleep(1)
        print("Send ACK ", window[count])
        ack += 1
    

receiver_socket.send("Final".encode())
receiver_socket.close() 