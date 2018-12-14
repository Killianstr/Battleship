import socket

UDP_IP = "10.160.108.9"
UDP_PORT = 5000
MESSAGE = "Hello, World!"

grille_client=[[0 for j in range(10)] for i in range(10)]

print(grille_client)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.connect((UDP_IP,UDP_PORT))

sock.send("connection possible ?".encode())

data=sock.recv(1024)
print(data.decode())
sens=input()
sock.send(sens.encode())

data=sock.recv(1024)
print(data.decode())
ligne=input()
sock.send(ligne.encode())

data=sock.recv(1024)
print(data.decode())
colonne=input()
sock.send(colonne.encode())

msg=""
while msg!="Fini" :
    msg=sock.recv(1024).decode()
    print(msg)
    if '?' in msg :
        reponse=input()
        sock.send(reponse.encode())
