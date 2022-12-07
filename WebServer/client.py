import os
import socket
import sys
import time


PATHNAME = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def est_connection():
    addr = "10.10.2.2"
    port = 5005
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((addr, port))
    except:
        print("destination could not be found.")
        sys.exit(1)
    replyStr = send_file(client)
    client.close()
    return replyStr


def send_file(client):
    for filename in os.listdir(PATHNAME):
        f = open(os.path.join(os.getcwd(),PATHNAME,filename), 'rb') 
        file_size = os.path.getsize(os.path.join(os.getcwd(),PATHNAME,filename))
        file_size = (str(file_size)).encode()
        start = time.perf_counter()

        client.send(file_size)
        # Reading file
        while True:
            data = f.read(1024)
            if not data:
                break
            byteSend = client.send(data)
            print(byteSend)
        f.close()
        print("file ", filename," has been sent.")
        replyStr = client.recv(1024)
        end = time.perf_counter()
        replyStr = replyStr.decode()
        # Need to add logic here to extract timestamp
        
        strs = replyStr.split(str=" ",num = 3)
        RTT = end - start
        transmission = RTT - strs[2]
        Tput = format(float(file_size)/float(RTT),".2f")
        print("Image is recognized as: ", replyStr)
        print("Rtt:" + RTT)
        print("Throughtput:" + Tput + "bytes/s")
        print("Transmission time:"+ transmission)
        return replyStr


if __name__ == '__main__':
    est_connection()
    
