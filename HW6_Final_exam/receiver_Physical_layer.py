import socket
import pickle
import time


def mlt_3_scheme_reverse(bitStream):
    result = ""
    for i in range(0, len(bitStream)):
        if i == 0:
            if bitStream[0] == '+':
                result += '1'
            else:
                result += '0'
        else:
            if bitStream[i] == bitStream[i - 1]:
                result += '0'
            else:
                result += '1'
        
    return result
    

def receiver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9993))
    server.listen()

    physical, addr = server.accept()
    print('Connect Physical layer\nHost IP:', addr[0], '\nPort:', addr[1])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9991))
    print('Connect Datalink layer')

    while True:
        packet = physical.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break

        print("message: " + data[0] + ", Packet: " + data[1])
        mlt = mlt_3_scheme_reverse(data[0])

        print("Reverse MLT-3 scheme : " + mlt + ", Packet: " + str(data[1]))
        time.sleep(1)
        message = [mlt, str(data[1])]
        data = pickle.dumps(message)
        client.send(data)


if __name__ == '__main__':
    receiver()