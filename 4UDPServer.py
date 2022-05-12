from socket import socket, AF_INET, SOCK_DGRAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))

print('The server is ready to receive')


while True:
    num, clientAddress = serverSocket.recvfrom(2048)
    print(num.decode())