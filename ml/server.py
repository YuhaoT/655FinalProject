import socket
import sys
import time
import googlenet


def start_connection():
    address = "127.0.0.1"
    port = 5005
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((address, port))
        s.listen()
    except:
        print('Failed to start connection')
        sys.exit(1)
    
    print ("opened on address {}, port {}, waiting for a connection".format(address, port))

    while True:
        sock, addr = s.accept()
        image_process(sock, addr)

def image_process(sock, addr):
    print ("connection accpeted {}:{}".format(addr[0],addr[1]))
    while True:
        data = sock.recv(1024)
        fp = open("image.jpg","wb")
        while True:
            data = sock.recv(1024000)
            if data == '':
                break
            fp.write(data)

        fp.close()
        start = time.perf_counter()
        replyStr = googlenet.image_predict("image.jpg")
        end = time.perf_counter()
        sock.sendall(replyStr + f" {start - end:0.4f} seconds")
        sock.close()
        break

if __name__ == '__main__':
    start_connection()
        


