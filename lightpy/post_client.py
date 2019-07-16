import socket
import os

sk = socket.socket()
address = ('127.0.0.1', 8080)

sk.connect(address)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.getcwd()

while True:
    ins = input('输入指令:').strip()  # post(上传命令) | xx.jpg

    comand, path = ins.split('|')

    path = os.path.join(BASE_DIR,path)

    filename = os.path.basename(path)
    filesizes = os.stat(path).st_size

    file_info = 'post|{}|{}'.format(filename,filesizes)

    sk.sendall(bytes(file_info,'utf8'))

    f = open(path,'rb')
    has_sent = 0
    while has_sent != filesizes:
        # read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)


    f.close()

    print("success")



