import socket

UDP_IP = "10.160.108.14"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True :
    data, addr = sock.recvfrom(1024)
    print ("received message :", data.decode())
    message=input("votre reponse : ")
    sock.sendto(message.encode(),addr)
    
