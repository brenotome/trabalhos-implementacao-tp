from socket import socket, AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Input lowercase sentence: or q to exit: ')
    if sentence == 'q':
        break
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
clientSocket.close()