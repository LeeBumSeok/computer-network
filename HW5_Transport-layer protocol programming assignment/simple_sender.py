import socket 

HOST = '127.0.0.1'
PORT = 9999

def send(sender, addr): 
    print('Connect \nHost ip:', addr[0], '\nPort:', addr[1]) 

    while True: 
        try:
            data = sender.recv(1024)

            if not data: 
                print('Disconnect')
                break

            print('Received Message: ', data.decode())

            sender.send(data) 

        except ConnectionResetError as e:
            print('Disconnect')
            break

    return False

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True: 
    print('server start')
    print('wait')

    sender, addr = server_socket.accept()
    if send(sender, addr) == False:
        sender.close()
        break
    
    


