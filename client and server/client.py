from socket import *

BUF_SIZE = 1024

while True:
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8080))
    data = input(">>")
    clientSock.sendall(data.encode())
    if(data == "bve"):
        clientSock.close()
        break
    res = clientSock.recv(1024)
    print(res.decode())