from socket import socket, AF_INET, SOCK_DGRAM
import select
import threading

def answer_requests(new_sock):
    '''
    Responde as requisições dos clients
    '''
    msg, address = new_sock.recvfrom(2048)
    if not msg:
        return
    response = str(msg, encoding='utf-8').upper()
    new_sock.sendto(response.encode(), address)

def server():
    serverPort = 12000

    with socket(AF_INET, SOCK_DGRAM) as sock:
        print('The server is ready to receive')
        sock.bind(('localhost', serverPort))
        # sock.listen(10)
        sock.setblocking(False)

        while True:
            read, _, _ = select.select([sock], [], [])
            for ready in read:
                client = threading.Thread(
                    target=answer_requests, args=(ready, )
                )
                client.start()


if __name__ == '__main__':
    server()