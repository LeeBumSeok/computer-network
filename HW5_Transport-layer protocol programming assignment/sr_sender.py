import socket 
import random
import time

HOST = '127.0.0.1'
PORT = 9999

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sender_socket.bind((HOST, PORT))
sender_socket.listen()

m = 3
size = (m ** 2) - 1

def send(sender, addr): 
    packet = 0
    print('Connect \nHost ip:', addr[0], '\nPort:', addr[1])
    window = list()
    for i in range(0, size + 1):
        window.append(i)

    while True:
        print("---------------------------------------")
        var = random.choice([True, False])
        if var:
            print("Send Packet ", packet)
            time.sleep(1)
        else:
            print("Lost Packet")
            print("Resend Packet")
            time.sleep(1)
            continue
        
        time.sleep(1)
        data = sender.recv(1024)
        if data.decode() == "Final":
            break
        ACK = int(data.decode()) % m
        countWin = 0
        print("receive ACK: ", ACK)
        print("sliding window: ", window[countWin], window[countWin + 1], window[countWin + 2], window[countWin + 3], ">>", window[countWin + 1], window[countWin + 2], window[countWin + 3], window[countWin + 4])
        countWin += 1
        if countWin > size:
            countWin -= size
        tmp = window[0]
        window.pop(0)
        window.append(tmp)
        
        if not data: 
            print('Disconnect')
            break

        count = 0

        while int(ACK) - 1 != packet:
            time.sleep(0.5)
            count += 1
            if count < 10:
                break
            continue


        sender.send(data)
        packet += 1
        if packet > m:
            packet -= m
        time.sleep(1)

    return False


while True: 
    print('server start')
    print('wait')

    sender, addr = sender_socket.accept()
    if send(sender, addr) == False:
        sender.close()
        print("Disconnect")
        break

