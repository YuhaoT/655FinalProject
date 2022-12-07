import socket
import sys
import time
import googlenet


def start_connection():
    address = "10.10.2.2"
    port = 5005
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((address, port))
        s.settimeout(30)
        s.listen()
    except:
        print('Failed to start connection')
        sys.exit(1)
    
    print ("opened on address {}, port {}, waiting for a connection".format(address, port))

    while True:
        try:
            sock, addr = s.accept()
            image_process(sock, addr)
        except socket.timeout:
            s.close()
            break

def image_process(sock, addr):
    print ("connection accpeted {}:{}".format(addr[0],addr[1]))
    while True:
        data = sock.recv(1024)
        filesize = int(data.decode())
        print ("initial data", filesize)
        cursize = 0
        fp = open("image.jpg","wb")
        print ("opened")
        data = sock.recv(1024)
        print (data)
        while True:
            fp.write(data)
            cursize += len(data)
            if cursize == filesize:
                break
            print (cursize)
            data = sock.recv(1024)
            print ("receiving ...")

        print ("file recieved")
            
        fp.close()
        start = time.perf_counter()
        replyStr = googlenet.image_predict("image.jpg")
        end = time.perf_counter()
        sock.sendall((replyStr + f" {end - start:0.4f} seconds").encode())
        sock.close()
        break

if __name__ == '__main__':
    start_connection()
        


