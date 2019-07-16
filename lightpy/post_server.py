import socket
import os

sk = socket.socket()

address = ('127.0.0.1', 8080)

sk.bind(address)
sk.listen(3)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('waiting.....')


while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        data = conn.recv(1024)
        comand, filename, filesize = str(data,'utf8').split('|')
        path = os.path.join(BASE_DIR,'photo',filename)
        filesize = int(filesize)


        f = open(path,'ab')
        has_recv = 0
        while has_recv != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_recv+=len(data)

        f.close()






