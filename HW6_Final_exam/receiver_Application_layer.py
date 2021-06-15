import socket
import pickle


def receiver():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(('', 9990))
    client.listen()

    transport, addr = client.accept()
    print('Connect Transport layer\nHost IP:', addr[0], '\nPort:', addr[1]) 

    while True:
        packet = transport.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break
            
        print("message: " + str(data[0]) + ", " + str(data[1]) + " reception")


if __name__ == '__main__':
    receiver()