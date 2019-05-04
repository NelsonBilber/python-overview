# echo server - client
# source code from here -> https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello from client script')
    data = s.recv(1024)

print ('Received reply(echo) from server: ', repr(data))