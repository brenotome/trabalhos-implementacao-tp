from socket import socket, AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print('para sair digite q')
while True:
    sentence = input('>')
    if sentence == 'q':
        break
    clientSocket.send(sentence.encode())
    response = clientSocket.recv(1024)
    if response == b'': #conn finalizada
        break
    print('< ', response.decode())
clientSocket.close()