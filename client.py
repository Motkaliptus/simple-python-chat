import socket
import threading

host = ''
port = 3000

client = socket.socket()
client.connect((host, port))

def receive():
    while True:
        msg = client.recv(1024).decode()
        print(msg)

def send():
    while True:
        msg = input('>>> ')
        if msg == '/exit':
            break
        msg = '\n' + msg
        client.send(msg.encode())
    client.close()

if __name__ == '__main__':
    threading.Thread(target=receive, daemon=True).start()
    send()