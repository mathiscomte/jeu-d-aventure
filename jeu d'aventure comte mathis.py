"""
Programme réalisé par comte, mathis, 1G4
"""
#desciption des pièces en fonction du numéro
def decrireLaPiece(piece):
    global clef
    global clef2
    global menu
    if piece==1:
        print("Vous vous trouvez dans le vestibule")
        if menu=='0':
            print("Entrez dans le cabanon pour gagner la partie")
    elif piece==2:
        print("Vous vous trouvez dans la salle à manger")
    elif piece==3:
        if clef==0:print("Vous vous trouvez dans la cuisine et vous venez de prendre la clé du grenier")
        else:print("Vous vous trouvez dans la cuisine")
    elif piece==4:
        print("Vous vous trouvez dans le salon")
    elif piece==5:
        print("Vous vous trouvez dans la bibliothèque")
    elif piece==6:
        print("Vous vous trouvez dans le garage")
    elif piece==7:
        print("Vous vous trouvez dans la véranda")
    elif piece==8:
        print("Vous vous trouvez dans le jardin")
    elif piece==9:
        print("Vous vous trouvez dans la chambre 1")
    elif piece==10:
        print("Vous vous trouvez dans le bureau")
    elif piece==11:
        print("Vous vous trouvez dans la salle de bain")
    elif piece==12:
        print("Vous vous trouvez dans la chambre 2")
    elif piece==13:
        if clef2==0:print("Vous vous trouvez dans le grenier et vous venez de prendre la clé du cabanon")
        else:print("Vous vous trouvez dans le grenier")
    elif piece==14:
        print("Vous vous trouvez dans le couloir")
    elif piece==15:
        print("Vous vous trouvez dans le cabanon, vous avez gagné la partie")


#la fonction decision ou "machine a état" permettant de se déplacer
#ou non en fonction de la pièce ou l'on se situe
def decision(direction,piece):
    global clef
    global clef2
    if direction=='n' or direction=='e' or direction=='s' or direction=='o':
        print("Vous désirez allez au",direction)
        memorisePiece=piece
        #N : le personnage désire aller au nord
        if direction=='n':
            if piece==1:
                piece=2
                intro=1
            elif piece==2:
                piece=14
            elif piece==6:
                if clef==1:
                    piece=13
            elif piece==7:
                piece=8
            elif piece==10:
                piece=5
            elif piece==14:
                piece=11
        #S : le personnage désire aller au sud
        elif direction=='s':
            if piece==2:
                piece=1
            elif piece==5:
                piece=10
            elif piece==8:
                piece=7
            elif piece==11:
                piece=14
            elif piece==13:
                piece=6
                clef2=1
            elif piece==14:
                piece=2
        #E : le personnage désire aller à l'est
        elif direction=='e':
            if piece==2:
                piece=3
            elif piece==3:
                piece=7
                clef=1
            elif piece==4:
                piece=2
            elif piece==6:
                piece=10
            elif piece==8:
                if clef2==1:
                    piece=15
            elif piece==10:
                piece=4
            elif piece==12:
                piece=14
            elif piece==14:
                piece=9
        #O : le personnage désire aller à l'ouest
        elif direction=='o':
            if piece==2:
                piece=4
            elif piece==3:
                piece=2
                clef=1
            elif piece==4:
                piece=10
            elif piece==7:
                piece=3
            elif piece==9:
                piece=14
            elif piece==10:
                piece=6
            elif piece==14:
                piece=12
            elif piece==15:
                piece=8
        if memorisePiece==piece:
            print("Déplacement impossible, il n'y a rien dans cette direction")
        else:
            print("C'est possible")
    elif direction!='q':
        print("Déplacement impossible, veuillez entrer une direction")
    return piece

#programme principal
dansQuellePieceEstLePersonnage=1   #variable très explicite
menu='0'
clef=0
clef2=0
rep='0'
while menu!='q':
    decrireLaPiece(dansQuellePieceEstLePersonnage)
    print("Ou désirez-vous aller? -------------------------------------")
    print("n : Nord")
    print("s : Sud")
    print("e : Est")
    print("o : Ouest")
    print("q : quitter")
    print("------------------------------------------------------------")
    menu=input("Quel est votre choix ?")
    dansQuellePieceEstLePersonnage=decision(menu,dansQuellePieceEstLePersonnage)
    if dansQuellePieceEstLePersonnage==15:
        decrireLaPiece(15)
        rep=input("Voulez-vous rejouer ?")
        while rep!='o' and rep!='n':
            rep=input("La réponse doit être 'o' ou 'n'")
        if rep=='o':
            dansQuellePieceEstLePersonnage=1
            menu='0'
            clef=0
            clef2=0
        elif rep=='n':
            menu='q'
print("Au revoir")
