import socket

UDP_IP = "10.160.108.10"
UDP_PORT = 5005
#message = "test"
UDP_IPC= "10.160.108.14"

while True :
    message=input("->")
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(message.encode(),(UDP_IPC, UDP_PORT))

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    print ("received message :", data)

