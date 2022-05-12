from socket import socket, AF_INET, SOCK_DGRAM

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

n:int = int(input('Quantos números ?'))
for i in range(1,n+1):    
    print(f'enviando {i}')
    clientSocket.sendto(str(i).encode(),(serverName, serverPort))

clientSocket.close()