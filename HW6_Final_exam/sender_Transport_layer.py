import time
import socket
import pickle

def sender():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9995))
    server.listen(1)

    sender_App, addr = server.accept()
    print('Connect Application layer\nHost IP:', addr[0], '\nPort:', addr[1])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9997))
    print('Connect Network layer') 

    count = 0

    while True:
        data = sender_App.recv(1024).decode()

        if (str(data)) == 'quit':
            client.send('Disconnect')
            print("Disconnect")
            server.close()
            break

        print("Send message: " + str(data))

        count = count + 1
        time.sleep(1)
        message = [str(data), str(count)]
        data = pickle.dumps(message)
        client.send(data)


if __name__ == '__main__':
    sender()


