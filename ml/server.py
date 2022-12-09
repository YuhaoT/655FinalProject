import socket
import sys
import time
import googlenet


def start_connection():
    address = "10.10.1.2"
    port = 80
    try:
        # opening socket and bind it on 10.10.1.2, and listening on port 80
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((address, port))
        s.settimeout(300)
        s.listen()
    except:
        print('Failed to start connection')
        sys.exit(1)
    
    print ("opened on address {}, port {}, waiting for a connection".format(address, port))

    # a loop that waits for connection
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
        # exchange file size
        data = sock.recv(1024)
        filesize = int(data.decode())
        print ("initial data", filesize)
        cursize = 0
        # open a file to write
        fp = open("image.jpg","wb")
        print ("opened")
        data = sock.recv(1024)
        print (data)
        while True:
            # receiving and writing image in chunks, break when cursize == filesize
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
        # invoke image processing program
        replyStr = googlenet.image_predict("image.jpg")
        end = time.perf_counter()
        # return result alongside processing time
        sock.sendall((replyStr + f" {end - start:0.4f} seconds").encode())
        sock.close()
        break

if __name__ == '__main__':
    start_connection()
        


