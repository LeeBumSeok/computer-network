import socket
import time


def sender():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9995))
    print('Connect Transport layer')

    message = str(input('Enter the message to send: '))

    if message == 'quit':
        print('Disconnect')
    else:
        while True:
            time.sleep(1)
            try:
                print("Send message: " + str(message))
                client.send(message.encode())
            except ConnectionResetError as e:
                print('The connection has been terminated.')
                break
            
    client.send(message.encode())
    client.close()


if __name__ == '__main__':
    sender()
