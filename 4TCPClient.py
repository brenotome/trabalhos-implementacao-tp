from socket import socket, AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

n:int = int(input('Quantos números ?'))
for i in range(1,n+1):    
    print(f'enviando {i}')
    clientSocket.send(str(i).encode())
clientSocket.close()