import socket
UDP_IP = "10.160.108.14" 
UDP_PORT = 5005
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT)) 
while True: 
    data, addr= sock.recvfrom(1024) # buffer size is1024 bytes 
    print(data.decode())
