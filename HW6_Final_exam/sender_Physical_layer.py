import socket
import pickle
import time

def mlt_3_scheme(bitStream):
    result = ""
    lastSign = "+"
    for i in range(0, len(bitStream) - 1):
        if i == 0:
            if bitStream[0] == "0":
                result += "0"
            else:
                result += "+"
                lastSign = "+"
        if bitStream[i + 1] == "0":
            result += result[-1]
        else:
            if result[-1] == "0":
                if lastSign == "+":
                    result += "+"
                    lastSign = "-"
                else:
                    result += ""
                    lastSign = "+"
            else:
                result += "0"

    return result


def sender():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9998))
    server.listen()

    sender, addr = server.accept()
    print('Connect Datalink layer\nHost IP:', addr[0], '\nPort:', addr[1])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9993))
    print('Connect Phycal layer') 

    while True:
        packet = sender.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break

        print("message: " + data[0] + ", Packet: " + data[1])

        mlt = mlt_3_scheme(data[0])
        print("Multi-transition MLT-3 scheme: " + mlt + ", Packet: " + str(data[1]))
        time.sleep(1)
        message = [mlt, str(data[1])]
        data = pickle.dumps(message)
        client.send(data)


if __name__ == '__main__':
    sender()