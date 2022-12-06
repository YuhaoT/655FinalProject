import os
import socket
import sys

PATHNAME = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def est_connection():
    addr = "127.0.0.1"
    port = 5005
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(addr, port)
    except:
        print("destination could not be found.")
        sys.exit(1)
    send_file(client)
    client.close()


def send_file(client):
    for filename in os.listdir(PATHNAME):
        with open(os.path.join(os.getcwd(),PATHNAME,filename), 'rb') as f:
            data = f.read(2048)
            while data:
                client.send(data)
                data = f.read(2048)
            client.send(data)
            f.close()
            print("file ", filename," has been sent.")
            replyStr = client.recv(1024)
            # Need to add logic here to extract timestamp
            print("Image is recognized as: ", replyStr)


if __name__ == '__main__':
    est_connection()
