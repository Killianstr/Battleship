import socket 

#Plateau de jeu des joueurs (le 1 pour le joueur coté client, le 2 pour le joueur coté serveur)
#--------------------------------------------------------------------------
client = 1
serveur = 2
bombe1 = [['1','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],]
bombe2 = [['2','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],]
bateau1 = [['1','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],]
bateau2 = [['2','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/'],]
#--------------------------------------------------------------------------

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
mesbateau = [4] # Taille du bateau
def placerbateau (joueur,addr,sock) :
    placebateau = "Place ton bateau"
    for i in range (len(mesbateau)) :
        if joueur == 2:
            taille = mesbateau[i]
            print (placebateau)
            position = input("->")
            flag = traitement(taille,position,joueur)
        elif joueur == 1:
            taille = mesbateau[i]
            sock.sendto(placebateau.encode(),addr)
            data, addr = sock.recvfrom(1024)
            flag = traitement(taille,data.decode(),joueur)     

        if flag == 0 :
            print ("problème de direction (Haut->h Bas->b Guauche->g Droite->d)")
        elif flag == 1 :
            print ("Ce bateau chevauche un autre bateau déja placé")
    return addr,sock 

def traitement(taille,position,joueur):
    licoldi = position.split(".")
    ligne = licoldi[0]
    ligne = int(ligne)
    licoldi = licoldi[1].split(" ")
    colonne = licoldi[0]
    colonne = int(colonne)
    direction = licoldi[1]

    if joueur == 1:
        bateau = bateau1
    elif joueur == 2:
        bateau = bateau2
    
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

#Programme principal qui lance les fonctions dans l'odre       
affichage(client)
addr,sock = placerbateau(client,addr,sock)
affichage(serveur)
addr,sock = placerbateau(serveur,addr,sock)
    


