import pickle
import socket

def receiver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9994))
    server.listen(1)

    network, addr = server.accept()
    print('Connect Network layer\nHost IP:', addr[0], '\nPort:', addr[1])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9990))
    print('Connect Application layer')

    while True:
        packet = network.recv(1024)

        try:
            data = pickle.loads(packet)
        except EOFError as e:
            print("Disconnect")
            client.close()
            break

        print("message: " + str(data[0]) + ", Packet: " + str(data[1]))
        message = [str(data[0]), "ACK"]

        print("Send Message : " + str(data[0]) + ", " + str(data[1]))
        data = pickle.dumps(message)
        client.send(data)


if __name__ == '__main__':
    receiver()

