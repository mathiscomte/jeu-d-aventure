"""
Programme réalisé par comte, mathis, 1G4
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
imgmaison = pygame.image.load("maison.jpg")
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("salle-a-manger.jpg")
image3=pygame.image.load("cuisine.jpg")
image4=pygame.image.load("salon.jpg")
image5=pygame.image.load("bibliotheque.jpg")
image6=pygame.image.load("garage.jpg")
image7=pygame.image.load("veranda.jpg")
image8=pygame.image.load("jardin.jpg")
image9=pygame.image.load("chambre1.jpg")
image10=pygame.image.load("bureau.jpg")
image11=pygame.image.load("salle-de-bain.jpg")
image12=pygame.image.load("chambre2.jpg")
image13=pygame.image.load("grenier.jpg")
image14=pygame.image.load("couloir.jpg")
image15=pygame.image.load("cabanon.jpg")
textmaison = font.render("Vous êtes sorti de la maison", True, (255, 255, 255))
text1 = font.render("Vous vous trouvez dans le vestibule", True, (255, 255, 255))
text2 = font.render("Vous vous trouvez dans la salle à manger", True, (255, 255, 255))
text3 = font.render("Vous vous trouvez dans la cuisine", True, (255, 255, 255))
text4 = font.render("Vous vous trouvez dans le salon", True, (255, 255, 255))
text5 = font.render("Vous vous trouvez dans la bibliothèque", True, (255, 255, 255))
text6 = font.render("Vous vous trouvez dans le garage", True, (255, 255, 255))
text7 = font.render("Vous vous trouvez dans la véranda", True, (255, 255, 255))
text8 = font.render("Vous vous trouvez dans le jardin", True, (255, 255, 255))
text9 = font.render("Vous vous trouvez dans la chambre 1", True, (255, 255, 255))
text10 = font.render("Vous vous trouvez dans le bureau", True, (255, 255, 255))
text11 = font.render("Vous vous trouvez dans la salle de bain", True, (255, 255, 255))
text12 = font.render("Vous vous trouvez dans la chambre 2", True, (255, 255, 255))
text13 = font.render("Vous vous trouvez dans le grenier", True, (255, 255, 255))
text14 = font.render("Vous vous trouvez dans le couloir", True, (255, 255, 255))
text15 = font.render("Vous vous trouvez dans le cabanon", True, (255, 255, 255))
textclef = font.render("Vous venez de prendre la clé du grenier", True, (255, 255, 0))
textclef2 = font.render("Vous venez de prendre la clé du cabanon", True, (255, 255, 0))
textintro = font.render("Jeu d'aventure", True, (255, 255, 0))
textintro2 = font.render("Entrez dans le cabanon pour gagner la partie !", True, (255, 255, 0))
textfin = font.render("Bravo, vous avez gagné !", True, (253,191, 0))
textrejouer = font.render("Voulez-vous rejouer ?",True, (253, 191, 0))
imgclef = pygame.image.load("clef.png")
imgclef2 = pygame.image.load("clef2.png")
cadre = pygame.image.load("cadre.png")


intro=0
dansQuellePieceEstLePersonnage=0
clef=0
clef2=0

def decrireLaPiece(piece):
    global intre
    global clef
    global clef2
    if piece==0:
        if intro==0:
            fenetre.blit(imgmaison,(0,0))
            fenetre.blit(textintro,(255,270))
            fenetre.blit(textintro2,(120,290))
        else:
            fenetre.blit(imgmaison,(0,0))
            fenetre.blit(textmaison,(10,300))
    elif piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(10,300))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(10,300))
    elif piece==3:
        if clef==0:
            fenetre.blit(image3,(0,0))
            fenetre.blit(text3,(10,300))
            fenetre.blit(textclef,(10,320))
        else:
            fenetre.blit(image3,(0,0))
            fenetre.blit(text3,(10,300))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(10,300))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(10,300))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(10,300))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(10,300))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(10,300))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(10,300))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(10,300))
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11,(10,300))
    elif piece==12:
        fenetre.blit(image12,(0,0))
        fenetre.blit(text12,(10,300))
    elif piece==13:
        if clef2==0:
            fenetre.blit(image13,(0,0))
            fenetre.blit(text13,(10,300))
            fenetre.blit(textclef2,(10,320))
        else:
            fenetre.blit(image13,(0,0))
            fenetre.blit(text13,(10,300))
    elif piece==14:
        fenetre.blit(image14,(0,0))
        fenetre.blit(text14,(10,300))
    elif piece==15:
        fenetre.blit(image15,(0,0))
        fenetre.blit(cadre,(173,150))
        fenetre.blit(text15,(10,300))
        fenetre.blit(textfin,(190,170))
        fenetre.blit(textrejouer,(200,190))
    if clef==1 or piece==3:
        fenetre.blit(imgclef,(0,0))
    if clef2==1 or piece==13:
        fenetre.blit(imgclef2,(60,0))



def decision(direction,piece):
    global clef
    global clef2
    global intro
    if direction=='n' or direction=='e' or direction=='s' or direction=='o':
        print("Vous désirez allez au",direction)
        memorisePiece=piece
        #N : le personnage désire aller au nord
        if direction=='n':
            if piece==0:
                piece=1
            elif piece==1:
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
            if piece==1:
                piece=0
                intro=1
            elif piece==2:
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
    elif direction=='q':
        print("Au revoir")
    else:
        print("Déplacement impossible, veuillez entrer une direction : n,s,o ou e")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePieceEstLePersonnage=decision(event.unicode,dansQuellePieceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePieceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
    if dansQuellePieceEstLePersonnage==15:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:  #lecture du clavier
                if event.unicode =='o':
                    dansQuellePieceEstLePersonnage=0
                    intro=0
                    clef=0
                    clef2=0
                elif event.unicode =='n':
                    loop=False
                elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                    loop = False
                else:print("La réponse doit être 'o' ou 'n'")


pygame.quit()

