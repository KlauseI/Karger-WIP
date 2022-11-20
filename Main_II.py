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
ORANGE = (238, 141, 14)
fenetre = pygame.display.set_mode(DIMENSION_FENETRE)
pygame.display.set_caption("Algorithme de Karger")

rect_20 = pygame.Rect(100, 350, 410, 70)
rect_200 = pygame.Rect(690, 350, 410, 70)
police_titre = pygame.font.SysFont('monospace', 30, True)

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

def stats():
    fichier = open('matrice2.txt')
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
    pygame.draw.circle(fenetre, ORANGE, (600, 60), 50)
    message_100x = police_titre.render("100X", True, NOIR)
    fenetre.blit(message_100x, (550, 50))

def main():
    time1 = time.time()
    graphe = {}
    Liste_coupe = []
    i = 100
    while i>0 :
        graphe = {}
        charger_graphe(graphe)
        Coupe_Min(graphe, Liste_coupe)
        i -= 1

    #print("Nombres de sommets avant algorithme: ", nb_sommet)#len(list(graphe.keys())))
    #print("Nombre d'aretes: ", nb_aretes/2)
    #print("Coupe minimale: ", min(Liste_coupe))
    #print("Coupe maximale: ", max(Liste_coupe))
    #print("Coupe moyenne: ", statistics.mean(Liste_coupe))

    stats()
    time2 = time.time()

    #print('Temps d execution: ', time2-time1)



while True:
    fenetre.fill(NOIR)
    afficher()
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







