#!usr/bin/python3

import socket, sys, errno

HOST = ''
PORT = 12345

try :

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #print('Socket successfully created')

except socket.error:
    print('Failed to create socket.')
    sys.exit()

try :

    server.bind((HOST,PORT))

except socket.error:
    print('Bind Failed.')

print("SSH Log-in Attempts")

while True:
    data = server.recv(1024).decode()
    print(data)

server.close()
