import socket 

#Connexion au client
#--------------------------------------------------------------------------
UDP_IP = "192.168.1.18"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print ("Attente de joueur")
data, addr = sock.recvfrom(1024)
print ("joueur trouvé")
#--------------------------------------------------------------------------