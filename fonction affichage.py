def affichage(joueur):
    UDP_IP = "10.160.108.14"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    if joueur == 1:
        bateau = bateau1
        bombe = bombe1
    elif joueur == 2:
        bateau = bateau2
        bombe = bombe2
    morp = ""
    message = "                  Bateau"
    if joueur == 1:
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    else :
        print (message)
    ligne="   0   1   2   3   4   5   6   7   8   9"
    if joueur == 1:
        sock.sendto(ligne.encode(), (UDP_IP, UDP_PORT))
    else :
        print(ligne)
    for i in range (10) :
        morp = str(i)+"| "
        for j in range (10) :
            morp += str(bateau[i][j])
            morp += " | "
        if joueur == 1:
            sock.sendto(morp.encode(), (UDP_IP, UDP_PORT))
        else:
            print(morp)
    morp = ""
    message = "                  Bombe"
    if joueur == 1:
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    else :
        print (message)
    if joueur == 1:
        sock.sendto(ligne.encode(), (UDP_IP, UDP_PORT))
    else :
        print(ligne)
    for i in range (10) :
        morp = str(i)+"| "
        for j in range (10) :
            morp += bombe[i][j]
            morp += " | "
        if joueur == 1:
            sock.sendto(morp.encode(), (UDP_IP, UDP_PORT))
        else :
            print(morp)
    espace="------------------------------------------"
    if joueur == 1:
        sock.sendto(espace.encode(), (UDP_IP, UDP_PORT))
    else :
        print(espace)

client = 1
serveur = 2
affichage(client)    #test affichage
affichage(serveur)
