from socket import socket, AF_INET, SOCK_DGRAM

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)


while True:
    message = input('Input lowercase sentence or "q" to exit:')
    if message == 'q':
        break
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

clientSocket.close()

"""
Apenas o client precisa ser alterado pois a conexão é UDP e não precisa de conexão
"""