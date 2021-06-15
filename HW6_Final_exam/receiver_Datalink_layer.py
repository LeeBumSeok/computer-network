import socket
import pickle
import time


        
def bitUnstuffing(frame):
    sequence = ""
    count = 0

    for i in range(0, len(frame)):
        if count != 5:
            sequence += frame[i]
        if frame[i] == '1':
            count += 1
        else:
            count = 0

    return sequence


def receiver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9991))
    server.listen()

    physical, addr = server.accept()
    print('Connect Physical layer\nHost IP:', addr[0], '\nPort:', addr[1]) 

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9992))
    print('Connect Network layer') 

    while True:
        packet = physical.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break

        print("message: " + str(data[0]) + ", Packet: " + str(data[1]))

        unstuffing = str(bitUnstuffing(data[0]))

        print("Bit-unstuffing Data : " + unstuffing + ", Packet: " + str(data[1]))
        time.sleep(1)
        message = [str(unstuffing), str(data[1])]
        data = pickle.dumps(message)
        client.send(data)

if __name__ == '__main__':
    receiver()

