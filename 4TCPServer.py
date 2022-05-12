from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive Numbers')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected to {addr}')
    while True:
        num = connectionSocket.recv(1)
        if num == b'':
            break
        print(num.decode())

    connectionSocket.close()