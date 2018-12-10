import socket

UDP_PORT = 5005
UDP_IP= "192.168.1.18"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto("1".encode(),(UDP_IP, UDP_PORT))

while True :
    data, addr = sock.recvfrom(1024)
    print (data.decode())

    message=input("->")
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(message.encode(),(UDP_IP, UDP_PORT))
