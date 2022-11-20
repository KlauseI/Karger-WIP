import random
import statistics
import time
import pygame
import sys


pygame.init()
DIMENSION_FENETRE = (1200, 760)  # en pixels
IPS = 25
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
BLANC = (255, 255, 255)
RED = (255, 0, 0)
fenetre = pygame.display.set_mode(DIMENSION_FENETRE)
pygame.display.set_caption("Algorithme de Karger")

rect_100x = pygame.Rect(550, 30, 100, 50)
police_titre = pygame.font.SysFont('monospace', 30, True)
police = pygame.font.SysFont('monospace',55, True)
police_stats = pygame.font.SysFont('monospace', 30, True)

mx, my = 0,0
graphe = {}
Liste_coupe = []
graphe2 = {}
Liste_coupe2 = []

def Coupe_Min(graphe,Liste_coupe):
    while len(graphe) > 2:
        # choisir deux sommets à 'fusionner'
        s1 = random.choice(list(graphe.keys()))
        # transforme les values des keys de graphe en listes == 1,2,3... et pick un nombre
        s2 = random.choice(graphe[s1])  # pick un sommet adjacent à s1


        # ajout de s2 dans s1
        for arete in graphe[s2]:  # les int ne sont pas necessaire si je jère le problème de s1/s2/arete et plus ??
            if arete != s1:
                graphe[s1].append(arete)
        # supprimer les connections a s2 et les mettres vers s1
        for arete in graphe[s2]:
            graphe[arete].remove(s2)
            if arete != s1:
                graphe[arete].append(s1)

        graphe.pop(s2)
    coupe = len(graphe[list(graphe.keys())[0]])
    Liste_coupe.append(coupe)


def charger_graphe(graphe):
    fichier = open('matrice2.txt')
    Liste_arete = []  # nb aretes par sommet
    for line in fichier:
        sommet = int(line.split()[0])  # donne le 1er élém de la ligne was int(line.split()[0])
        aretes = []
        for arete in line.split()[1:]:
            aretes.append(int(arete))
        graphe[sommet] = aretes
        # nb_aretes += len(aretes)
        Liste_arete.append(len(aretes))
    fichier.close()

def stats(nom):
    fichier = open(nom)
    min_deg = 0
    max_deg = 0
    nb_aretes = 0
    nb_sommets = 0
    tmp = 0
    flag = 1
    liste_aretes = {}  # sert a quoi ?
    for line in fichier:

        nb_sommets += 1
        tmp = 0
        for arete in line.split()[1:]:
            tmp += 1
            nb_aretes += 1
        if int(line[0]) == 1 and flag:
            min_deg = tmp
            max_deg = tmp
            flag = 0
            flag = 0
        if tmp > max_deg:
            max_deg = tmp
        if tmp < min_deg:
            min_deg = tmp
    fichier.close()
    #print('Degre minimal: ', min_deg)
    #print('Degre maximal: ', max_deg)
    #print('Nombre de sommets: ', nb_sommets)
    #print('Nombre d aretes: ', nb_aretes)
    return mind_deg, max_deg, nb_sommets, nb_aretes

def afficher():
    pygame.draw.rect(fenetre, RED, rect_100x)
    message_100x = police_titre.render("100X", True, NOIR)
    fenetre.blit(message_100x, (563, 38))
    message_20_sommets = police.render("20 Sommets", True, BLANC)
    fenetre.blit(message_20_sommets, (115,25))
    message_200_sommets = police.render("200 Sommets", True, BLANC)
    fenetre.blit(message_200_sommets, (730, 25))
    rect_20 = pygame.Rect(115, 85, 330, 10)
    pygame.draw.rect(fenetre, RED, rect_20)
    rect_200 = pygame.Rect(730, 85, 365, 10)
    pygame.draw.rect(fenetre, RED, rect_200)

    fenetre.blit(write("Sommets",200,RED)[0],write("Sommets",200,RED)[1])
    fenetre.blit(write("Arêtes", 270, RED)[0], write("Arêtes", 270, RED)[1])
    fenetre.blit(write("Degré min", 340, RED)[0], write("Degré min", 340, RED)[1])
    fenetre.blit(write("Degré max", 410, RED)[0], write("Degré min", 410, RED)[1])

    fenetre.blit(write("Coupe min", 480, RED)[0], write("Coupe min", 480, RED)[1])
    fenetre.blit(write("Coupe max", 550, RED)[0], write("Coupe max", 550, RED)[1])
    fenetre.blit(write("Coupe moyenne", 620, RED)[0], write("Coupe moyenne", 620, RED)[1])
    fenetre.blit(write("Temps d'exécution", 690, RED)[0], write("Temps d'exécution", 690, RED)[1])


    if not flag:
        pass
def write(text, y, couleur):
    text = police_stats.render(text, True, couleur)
    text_rect = text.get_rect(center=(1200//2, y))
    return text, text_rect


def position_souris():
    global mx,my,rect_100x
    if rect_100x.collidepoint((mx, my)):
        if flag:
            flag = False
            main(graphe, Liste_coupe,'matrice.txt')
        else:
            main(graphe2, Liste_coupe2, 'matrice2.txt')


def main(graphe, Liste_coupe, nom):
    time1 = time.time()
    i = 100
    while i>0 :
        graphe = {}
        charger_graphe(graphe)
        Coupe_Min(graphe, Liste_coupe)
        i -= 1

    #print("Coupe minimale: ", min(Liste_coupe))
    #print("Coupe maximale: ", max(Liste_coupe))
    #print("Coupe moyenne: ", statistics.mean(Liste_coupe))

    stats(nom)
    time2 = time.time()

    #print('Temps d execution: ', time2-time1)


flag = True
while True:
    fenetre.fill(NOIR)
    afficher()
    mx, my = pygame.mouse.get_pos()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    pygame.time.Clock().tick(IPS)







