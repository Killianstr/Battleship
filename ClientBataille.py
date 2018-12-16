import socket

UDP_PORT = 5005
UDP_IP= "192.168.1.18"

bombe = [[" " for j in range(10)] for i in range(10)]
bateau = [[" " for j in range(10)] for i in range(10)]

#Lancement de la partie
#--------------------------------------------------------------------------
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect((UDP_IP,UDP_PORT))

go = input("Lancer une partie (1) pour oui : ")
sock.send(go.encode())
#--------------------------------------------------------------------------

#Fonction affichage
#--------------------------------------------------------------------------
def affichage ():
    morp = ""
    print ("                  Bateau")
    ligne="   0   1   2   3   4   5   6   7   8   9"
    print(ligne)
    for i in range (10) :
        morp = str(i)+"| "
        for j in range (10) :
            morp += str(bateau[i][j])
            morp += " | "
        print(morp)
    morp = ""
    print ("                  Bombe")
    print(ligne)
    for i in range (10) :
        morp = str(i)+"| "
        for j in range (10) :
            morp += bombe[i][j]
            morp += " | "
        print(morp)
    print("------------------------------------------")
#--------------------------------------------------------------------------

#Placer bateau
#--------------------------------------------------------------------------
def placerbateau (ligne,colonne,direction):
    ligne = int(ligne)
    colonne = int(colonne)
    taille = 4 #Taille de l'unique bateau à modifier pour plusieurs bateaux
    
    if (direction == "h") and ((taille+ligne+1) > 7) :
        for i in range (0,taille) :
            if (bateau[ligne-i][colonne]) == "=" :
                return 1
        for j in range (0,taille) :
            bateau[ligne-j][colonne] = "="
    elif (direction == "b") and ((taille+ligne+1) <= 11) :
        for i in range (0,taille) :
            if (bateau[ligne+i][colonne]) == "=" :
                return 1
        for j in range (0,taille) :
            bateau[ligne+j][colonne] = "="
    elif (direction == "g") and ((taille+colonne+1) > 7) :
        for i in range (0,taille) :
            if (bateau[ligne][colonne-i]) == "=" :
                return 1
        for j in range (0,taille) :
            bateau[ligne][colonne-j] = "="
    elif (direction == "d") and ((taille+colonne+1) <= 11) :
        for i in range (0,taille) :
            if (bateau[ligne][colonne+i]) == "=" :
                return 1 
        for j in range (0,taille) :
            bateau[ligne][colonne+j] = "="
    else:
        return 0
#--------------------------------------------------------------------------

#Script de la partie
#--------------------------------------------------------------------------
affichage ()

data = sock.recv(1024)
print (data.decode())

ligne = input("Ligne -> ")
sock.send(ligne.encode())

colonne = input("Colonne -> ")
sock.send(colonne.encode())

direction = input("Direction (Haut->h Bas->b Guauche->g Droite->d) ->")
sock.send(direction.encode())

placerbateau (ligne,colonne,direction)
affichage ()

msg=""
while msg!="Fini" :
    msg=sock.recv(1024).decode()
    print(msg)
    if '?' in msg :
        reponse=input("->")
        sock.send(reponse.encode())
        
data=sock.recv(1024)
print(data.decode())
#--------------------------------------------------------------------------
