import socket 

#Plateau de jeu des joueurs (le 1 pour le joueur coté client, le 2 pour le joueur coté serveur)
#--------------------------------------------------------------------------
client = 1
serveur = 2
bombe1 = [[" " for j in range(10)] for i in range(10)]
bateau1 = [[" " for j in range(10)] for i in range(10)]
bombe2 = [[" " for j in range(10)] for i in range(10)]
bateau2 = [[" " for j in range(10)] for i in range(10)]
mesbateau = [4] # Taille du bateau
pointclient = 0
pointserveur = 0
#--------------------------------------------------------------------------

#Connexion au client
#--------------------------------------------------------------------------
UDP_IP = "10.160.108.14"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print ("Attente de joueur")
data, addr = sock.recvfrom(1024)
print ("joueur trouvé")
#--------------------------------------------------------------------------

#Fonction affichage
#--------------------------------------------------------------------------
def affichage(joueur):
    if joueur == 1:
        print ("[client]")
        bateau = bateau1
        bombe = bombe1
    elif joueur == 2:
        print ("[serveur]")
        bateau = bateau2
        bombe = bombe2
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

#Fonction placer bateau comprenant le fonction traitement
#--------------------------------------------------------------------------
def placerbateau (joueur,addr,sock) :
    if joueur == 2:
        bateau = bateau2
        print ("Place ton bateau")
    elif joueur == 1:
        bateau = bateau1
        sock.sendto("Place ton bateau".encode(),addr)
    for i in range (len(mesbateau)) :
        if joueur == 2:
            taille = mesbateau[i]
            ligne = input("Ligne -> ")
            colonne = input("Colonne -> ")
            direction = input("Direction (Haut->h Bas->b Guauche->g Droite->d) -> ")
            
        elif joueur == 1:
            taille = mesbateau[i]
            
            data, addr = sock.recvfrom(1024)
            ligne = data.decode()
            data, addr = sock.recvfrom(1024)
            colonne = data.decode()
            data, addr = sock.recvfrom(1024)
            direction = data.decode()
            
        ligne = int(ligne)
        colonne = int(colonne)
        flag = 0
    
        if (direction == "h") and ((taille+ligne+1) > 7) :
            for i in range (0,taille) :
                if (bateau[ligne-i][colonne]) == "=" :
                    flag = 1
            for j in range (0,taille) :
                bateau[ligne-j][colonne] = "="
        elif (direction == "b") and ((taille+ligne+1) <= 11) :
            for i in range (0,taille) :
                if (bateau[ligne+i][colonne]) == "=" :
                    flag = 1
            for j in range (0,taille) :
                bateau[ligne+j][colonne] = "="
        elif (direction == "g") and ((taille+colonne+1) > 7) :
            for i in range (0,taille) :
                if (bateau[ligne][colonne-i]) == "=" :
                    flag = 1
            for j in range (0,taille) :
                bateau[ligne][colonne-j] = "="
        elif (direction == "d") and ((taille+colonne+1) <= 11) :
            for i in range (0,taille) :
                if (bateau[ligne][colonne+i]) == "=" :
                    flag = 1 
            for j in range (0,taille) :
                bateau[ligne][colonne+j] = "="
        else:
            flag = 0    

        if flag == 0 :
            print ("problème de direction (Haut->h Bas->b Guauche->g Droite->d)")
        elif flag == 1 :
            print ("Ce bateau chevauche un autre bateau déja placé")
    return addr,sock 

#--------------------------------------------------------------------------

#Fonction placer Bombe
#--------------------------------------------------------------------------
def placerbombe (joueur , point, addr, sock) :
    if joueur == 2 :
        ligne = int(input("Position de la ligne de tir ? "))
        colonne = int(input("Position de la colonne de tir ? "))

        if bateau1[ligne][colonne] == "=":
            print ("====>Bateau adverse touché<====")
            sock.sendto("====>Votre bateau est touché<====".encode(), addr)
            point += 1
            bateau1[ligne][colonne]="X"
            bombe2[ligne][colonne]="X"
            
        elif bateau1[ligne][colonne] == "X":
            print ("====>Bateau déja touché<====")
            sock.sendto("====>Votre adversaire à raté son tire<====".encode(), addr)

        elif bateau1[ligne][colonne] == "*":
            print ("====>Tire déja raté<====")
            sock.sendto("====>Votre adversaire à raté son tire<====".encode(), addr)

        else :
            bateau1[ligne][colonne]="*"
            bombe2[ligne][colonne]="*"
            print ("====>Bateau raté<====")
            sock.sendto("====>Votre adversaire à tiré dans l'eau<====".encode(), addr)
            
    elif joueur == 1 :
        sock.sendto("Ligne de tir ? ".encode(), addr)
        data, addr = sock.recvfrom(1024)
        ligne = int (data.decode())


        sock.sendto("Colonne de tir  ? ".encode(), addr)
        data, addr = sock.recvfrom(1024)
        colonne = int (data.decode())

        if bateau2[ligne][colonne] == "=":
            print ("====>Votre bateau est touché<====")
            sock.sendto("====>Bateau adverse touché<====".encode(), addr)
            point += 1
            bateau2[ligne][colonne]= "X"
            bombe1[ligne][colonne]= "X"

        elif bateau2[ligne][colonne] == "X":
            print ("====>Votre adversaire à raté son tire<====")
            sock.sendto("====>Bateau déja touché<====".encode(), addr)

        elif bateau2[ligne][colonne] == "*":
            print ("====>Votre adversaire à raté son tire<====")
            sock.sendto("====>Tire déja raté<====".encode(), addr)

        else :
            bateau2[ligne][colonne]="*"
            bombe1[ligne][colonne]="*"
            print("====>Votre adversaire à tiré dans l'eau<====")
            sock.sendto("====>Bateau raté<====".encode(), addr)
        
    return addr,sock,point
#--------------------------------------------------------------------------


#Programme principal qui lance les fonctions dans l'odre
affichage(serveur)
addr,sock = placerbateau(client,addr,sock)
addr,sock = placerbateau(serveur,addr,sock)
affichage(serveur)

while pointclient <4 and pointserveur <4 : #A modifier pour plusieurs bateaux 
    addr,sock,pointserveur = placerbombe (serveur , pointserveur,addr, sock)
    affichage(serveur)  
    addr,sock,pointclient = placerbombe (client , pointclient,addr, sock)
    affichage(serveur)  

    print ("-------------------")
    print ("Point client  :",pointclient,"|")
    print ("Point serveur :",pointserveur,"|")
    print ("-------------------")

print("Fin de la game")
sock.sendto("Fin de la game".encode(), addr)


