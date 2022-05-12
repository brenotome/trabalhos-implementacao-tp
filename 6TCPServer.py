from socket import socket, AF_INET, SOCK_STREAM

def finalizing_state(sock, previous_message=''):
    sock.send(f'{previous_message}Obrigado por utilizar nossos serviços! Até logo!'.encode())

def greeting_state(sock):    
    sock.send('Olá Bem-vindo! Qual o seu nome ?'.encode())   
    name = sock.recv(10240).decode()
    service_state(sock, name)


def service_state(sock, name):
    states = {
        1: monitoring_state,
        2: activities_state,
        3: mailing_state
    }

    sock.send(f'Certo, {name}! Como posso te ajudar? Digite o número que corresponde a opção desejada:\n \
        1 - Agendar um horário de monitoria \n\
        2 - Listar as próximas atividades da disciplina \n \
        3 - E-mail do professor'.encode())
    op = int(sock.recv(1).decode())
    if op not in [1,2,3]:
        finalizing_state(sock)
    states[op](sock)


def monitoring_state(sock):
    msg = 'Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br\n'
    finalizing_state(sock, msg)


def activities_state(sock):
    msg = 'Fique atento para as datas das próximas atividades. Confira o que vem por aí! \n\n\
        P1: 26 de maio de 2022 \n \
        Lista 3: 29 de maio de 2022 '
    finalizing_state(sock, msg) 


def mailing_state(sock):
    msg = 'Quer falar com o professor? \
        O e-mail dele é sadoc@dcc.ufrj.br'
    finalizing_state(sock, msg)


def server():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive messages')

    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f'Connected to {addr}')
        connectionSocket.recv(10240).decode()
        greeting_state(sock=connectionSocket)
        connectionSocket.close()
        print('Connection ended, now listening')        

if __name__ == '__main__':
    server()