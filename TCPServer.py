from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected to {addr}')
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == '':
            # if the connection is stopped the server will receive an empty sentence
            print('Connection ended, now listening')
            break
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()