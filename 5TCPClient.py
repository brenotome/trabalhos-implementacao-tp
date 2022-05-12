from getpass import getpass
from socket import socket, AF_INET, SOCK_STREAM


serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

username = input('digite seu nome de usuário:')
password = getpass('digite sua senha: ')

clientSocket.send((':'.join([username,password])).encode())
response = clientSocket.recv(1024).decode()
print(response)
clientSocket.close()