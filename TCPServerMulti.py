import select
from socket import socket, AF_INET, SOCK_STREAM
import threading


def server():
    '''
    inicia o servidor
    '''
    serverPort = 12000
    with socket(AF_INET, SOCK_STREAM) as sock:
        print("listening")
        sock.bind(('localhost', serverPort))
        sock.listen(10)
        sock.setblocking(False)

        while True:
            read, _, _ = select.select([sock], [], [])
            for ready in read:
                connection, address = ready.accept()
                client = threading.Thread(
                    target=answer_requests, 
                    args=(connection, address))
                client.start()


def answer_requests(connection, address):
    '''
    Responde as requisições dos clients
    '''
    with connection:
        while True:
            msg = connection.recv(1024)
            if not msg:
                break
            response = str(msg, encoding='utf-8').upper()
            connection.send(response.encode())


if __name__ == '__main__':
    server()

