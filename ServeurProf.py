import socket

UDP_IP = "10.160.108.9"
UDP_PORT = 5000

grille_client = [[0 for j in range(10)] for i in range(10)]
point_client = 0
point_serveur = 0

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
if addr :
    print("Client connecté")
print("Message recu :", data.decode())
sock.sendto("Quel sens (H ou V)?".encode(), addr)
data, addr = sock.recvfrom(1024)
sens=data.decode()
if sens == "H":
    print("Position horizontale choisie")

elif sens == "V":
    print("Position verticale choisie")

sock.sendto("Quelle ligne?".encode(), addr)
data, addr = sock.recvfrom(1024)
ligne = int (data.decode())
print ("Ligne =", ligne)

sock.sendto("Quelle colonne?".encode(), addr)
data, addr = sock.recvfrom(1024)
colonne = int(data.decode())
print ("colonne =", colonne)                   

if sens == "H":
    grille_client[ligne][colonne] = 1
    grille_client[ligne][colonne+1] = 1
    grille_client[ligne][colonne+2] = 1
    grille_client[ligne][colonne+3] = 1

if sens == "V":
    grille_client[ligne][colonne] = 1
    grille_client[ligne+1][colonne] = 1
    grille_client[ligne+2][colonne] = 1
    grille_client[ligne+3][colonne] = 1

for ligne in grille_client:
    print (ligne)

grille_serveur = [[0 for j in range(10)] for i in range(10)]

sens = input ("Quelle sens (H ou V)?")
if sens == "H":
    print("Position horizontale choisie")

elif sens == "V":
    print("Position verticale choisie")

ligne = int( input ("Quelle ligne?"))
print ("Ligne =",ligne)

colonne = int(input ("Quelle colonne?"))
print("Colonne =", colonne)
    
if sens == "H":
    grille_serveur[ligne][colonne] = 1
    grille_serveur[ligne][colonne+1] = 1
    grille_serveur[ligne][colonne+2] = 1
    grille_serveur[ligne][colonne+3] = 1

if sens == "V":
    grille_serveur[ligne][colonne] = 1
    grille_serveur[ligne+1][colonne] = 1
    grille_serveur[ligne+2][colonne] = 1
    grille_serveur[ligne+3][colonne] = 1

for ligne in grille_serveur:
    print (ligne)

while point_client <4 and point_serveur <4 :
        
    sock.sendto("Ligne de tir?".encode(), addr)
    data, addr = sock.recvfrom(1024)
    ligne_tir=int (data.decode())


    sock.sendto("Colonne de tir?".encode(), addr)
    data, addr = sock.recvfrom(1024)
    colonne_tir=int (data.decode())

    if grille_serveur[ligne_tir][colonne_tir] == 1:
        print ("cible touché")
        sock.sendto("Cible touché".encode(), addr)
        point_client=point_client+1
        grille_serveur[ligne_tir][colonne_tir]=2

    else :
        print  ("Cible raté")
        sock.sendto("Cible raté".encode(), addr)
            

    ligne_tir = int(input("Position de la ligne de tir?"))
    colonne_tir = int(input("Position de la colonne de tir?"))


    if grille_client[ligne_tir][colonne_tir] == 1:
        print ("cible touché")
        sock.sendto("Cible touché".encode(), addr)
        point_serveur=point_serveur+1
        grille_client[ligne_tir][colonne_tir]=2

    else :
        print ("Cible raté")
        sock.sendto("Cible raté".encode(), addr)
    print ("Point client :",point_client)
    print ("Point serveur :",point_serveur)

sock.sendto("Fini".encode(),addr)
print ("Fini")

