from socket import socket, AF_INET, SOCK_STREAM

def auth(username, password):
    if username == 'user' and password == 'pass':
        return True
    else: 
        return False

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('Login server UP')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected to {addr}')    

    message = connectionSocket.recv(1024).decode()
    try:
        username, password = message.split(':')
        if auth(username, password):
            connectionSocket.send('Login bem sucedido \n A reposta é 42'.encode())
        else:
            connectionSocket.send('Dados incorretos'.encode())
    except:
        print('bad message')
        break    

    connectionSocket.close()