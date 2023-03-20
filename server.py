import socket
import threading

host = ''
port = 3000

server = socket.socket()
server.bind((host, port))

server.listen()
print('[+] En espera de conexiones...')
client, addr= server.accept()
print(f'[+] {addr[0]} se ha conectado')
client.send('[+] Conectado al servidor'.encode())

def send():
    while True:
        msg = input('>>> ')
        if msg == '/exit':
            break
        msg = '\n' + msg
        client.send(msg.encode())

    client.close()
    server.close()

def receive():
    while True:
        msg = client.recv(1024).decode()
        print(msg)

if __name__ == '__main__':
    threading.Thread(target=receive, daemon=True).start()
    send()
    
