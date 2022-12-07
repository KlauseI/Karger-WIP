import random
import statistics
import time
import pygame
import sys

#####   PARAMETRES  #####
pygame.init()
DIMENSION_FENETRE = (1200, 760)
IPS = 30
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


#####   Variables   #####
mx, my = 0,0

# variables pour 20 sommets
graphe = {}
Liste_coupe = []
temps20 = 0
dic20 = {'sommets':0,'aretes':0,'aretes':0,'min_deg':0,'max_deg':0,'min':0,'max':0,'moy':0}

# variables pour 200 sommets
graphe2 = {}
Liste_coupe2 = []
dic200 = {'sommets':0,'aretes':0,'aretes':0,'min_deg':0,'max_deg':0,'min':0,'max':0,'moy':0}
temps200 = 0

# Algorithme de Karger
def Coupe_Min(graphe,Liste_coupe):
    while len(graphe) > 2:
        # choisir deux sommets à 'fusionner'
        s1 = random.choice(list(graphe.keys()))
        # transforme les values des keys de graphe en listes == 1,2,3... et pick un nombre
        s2 = random.choice(graphe[s1])  # pick un sommet adjacent à s1


        # ajout de s2 dans s1
        for arete in graphe[s2]:
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


def charger_graphe(graphe,bool):
    if bool:
        nom = 'matrice.txt'
        fichier = open(nom)
    else:
        nom = 'matrice2.txt'
        fichier = open(nom)

    for line in fichier:
        sommet = int(line.split()[0])
        aretes = []
        for arete in line.split()[1:]:
            if int(arete) != sommet:
                aretes.append(int(arete))
        graphe[sommet] = aretes

    fichier.close()

    nb = stats(nom)[2]
    connexite = [0] * nb
    for i in range(1, nb + 1):
        for value in graphe[i]:
            connexite[value - 1] = 1

    for j in range(0, nb):
        if not connexite[j]:
            sys.exit('Le graphe n est pas connexe')


def est_connexe(graphe,fichier):
    nb = stats(fichier)[2]
    connexite = [0]*nb
    for i in range(1,nb+1):
        for value in graphe[i]:
            connexite[value-1] = 1

    for j in range(0,nb):
        if not connexite[j]:
            sys.exit('Le graphe n est pas connexe')


def stats(nom):
    fichier = open(nom)
    min_deg = 0
    max_deg = 0
    nb_aretes = 0
    nb_sommets = 0
    tmp = 0
    flag = 1

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
        if tmp > max_deg:
            max_deg = tmp
        if tmp < min_deg:
            min_deg = tmp
    fichier.close()

    return min_deg, max_deg, nb_sommets, nb_aretes

def afficher(dic20, dic200, temps20, temps200):

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

    fenetre.blit(write("Sommets", 600, 200, RED)[0],write("Sommets", 600, 200, RED)[1])
    fenetre.blit(write("Arêtes", 600, 270, RED)[0], write("Arêtes",600, 270, RED)[1])
    fenetre.blit(write("Degré min", 600, 340, RED)[0], write("Degré min", 600, 340, RED)[1])
    fenetre.blit(write("Degré max", 600, 410, RED)[0], write("Degré min", 600, 410, RED)[1])

    fenetre.blit(write("Coupe min", 600, 480, RED)[0], write("Coupe min", 600, 480, RED)[1])
    fenetre.blit(write("Coupe max", 600, 550, RED)[0], write("Coupe max", 600, 550, RED)[1])
    fenetre.blit(write("Coupe moyenne", 600, 620, RED)[0], write("Coupe moyenne", 600, 620, RED)[1])
    fenetre.blit(write("Temps d'exécution", 600, 690, RED)[0], write("Temps d'exécution", 600, 690, RED)[1])

    # Valeurs pour 20 sommets
    fenetre.blit(police_stats.render(str(dic20['sommets']), True, BLANC),(300,180))
    fenetre.blit(police_stats.render(str(dic20['aretes']), True, BLANC), (300, 250))
    fenetre.blit(police_stats.render(str(dic20['min_deg']), True, BLANC), (300, 320))
    fenetre.blit(police_stats.render(str(dic20['max_deg']), True, BLANC), (300, 390))
    fenetre.blit(police_stats.render(str(dic20['min']), True, BLANC), (300, 460))
    fenetre.blit(police_stats.render(str(dic20['max']), True, BLANC), (300, 530))
    fenetre.blit(police_stats.render(str(dic20['moy']), True, BLANC), (300, 600))
    fenetre.blit(police_stats.render(str(temps20), True, BLANC), (300, 670))

    # valeurs pour 200 sommets
    fenetre.blit(police_stats.render(str(dic200['sommets']), True, BLANC), (900, 180))
    fenetre.blit(police_stats.render(str(dic200['aretes']), True, BLANC), (900, 250))
    fenetre.blit(police_stats.render(str(dic200['min_deg']), True, BLANC), (900, 320))
    fenetre.blit(police_stats.render(str(dic200['max_deg']), True, BLANC), (900, 390))
    fenetre.blit(police_stats.render(str(dic200['min']), True, BLANC), (900, 460))
    fenetre.blit(police_stats.render(str(dic200['max']), True, BLANC), (900, 530))
    fenetre.blit(police_stats.render(str(dic200['moy']), True, BLANC), (900, 600))
    fenetre.blit(police_stats.render(str(temps200), True, BLANC), (900, 670))

def menu_presentation():
    pass

def write(text, x, y, couleur):
    text = police_stats.render(text, True, couleur)
    text_rect = text.get_rect(center=(x, y))
    return text, text_rect


def position_souris():
    global mx,my,rect_100x,flag,peut_clicker
    if rect_100x.collidepoint((mx, my)):
        if flag:
            main(graphe, Liste_coupe, 1)
            flag = False
            maj('matrice.txt',dic20,dic200,Liste_coupe, Liste_coupe2)
        elif not flag and peut_clicker:
            main(graphe2, Liste_coupe2, 0)
            maj('matrice2.txt',dic20,dic200,Liste_coupe, Liste_coupe2)
            peut_clicker = False

def maj(nom,dic20,dic200,Liste_coupe,Liste_coupe2):
    if nom == 'matrice.txt':
        dic20['sommets'] = stats(nom)[2]
        dic20['aretes'] = stats(nom)[3]
        dic20['min_deg'] = stats(nom)[0]
        dic20['max_deg'] = stats(nom)[1]
        dic20['min'] = min(Liste_coupe)
        dic20['max'] = max(Liste_coupe)
        dic20['moy'] = statistics.mean(Liste_coupe)
    else:
        dic200['sommets'] = stats(nom)[2]
        dic200['aretes'] = stats(nom)[3]
        dic200['min_deg'] = stats(nom)[0]
        dic200['max_deg'] = stats(nom)[1]
        dic200['min'] = min(Liste_coupe2)
        dic200['max'] = max(Liste_coupe2)
        dic200['moy'] = statistics.mean(Liste_coupe2)




def main(graphe, Liste_coupe,bool):
    global flag,temps20,temps200
    temps1 = time.time()
    i = 100
    while i>0 :
        graphe = {}
        charger_graphe(graphe,bool)
        Coupe_Min(graphe, Liste_coupe)
        i -= 1

    temps2 = time.time()
    if flag:
        temps20 = temps2 - temps1
        temps20 = round(temps20, 4)
    if not flag:
        temps200 = temps2 - temps1
        temps200 = round(temps200, 4)


flag = True
peut_clicker = True # pour ne pas lancer plusieurs fois l'algo
while True:
    fenetre.fill(NOIR)
    afficher(dic20,dic200,temps20,temps200)
    mx, my = pygame.mouse.get_pos()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if evenement.button == 1:
                position_souris()
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    pygame.time.Clock().tick(IPS)








