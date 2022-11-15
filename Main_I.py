import random
import math
import statistics

def Coupe_Min(graphe,Liste_coupe):
    while len(graphe) > 2:
        # choisir deux sommets à 'fusionner'
        s1 = random.choice(list(graphe.keys()))
        s2 = random.choice(graphe[s1])  # pick un sommet adjacent à s1
        print(graphe)
        print('s1=', s1)
        print('s2=', s2)

        # ajout de s2 dans s1
        for arete in graphe[s2]:  # les int ne sont pas necessaire si je jère le problème de s1/s2/arete et plus ??
            if arete != s1 :
                graphe[s1].append(arete)
        print('graphe apres ajout=', graphe)
        # supprimer les connections a s2 et les mettres vers s1
        for arete in graphe[s2]:
            graphe[arete].remove(s2) # was graphe[arete].remove(s2)
            if arete != s1 :
                graphe[arete].append(s1)

        graphe.pop(s2)
    print('graphe apres remove=', graphe)
    coupe = len(graphe[list(graphe.keys())[0]])
    print('coupe =', coupe)
    Liste_coupe.append(coupe)

def main():
    # charger le fichier + init des variables
    fichier = open('matrice2.txt')
    graphe = {}  # chaque elem = liste des sommets adjacents, nb: graphe[0] est vide
    # sommet 1 = sa liste de sommets adjacents ! dictionnaire : key = value, pas une liste banale.
    nb_aretes = 0  # nb globale d aretes
    Liste_arete = []  # nb aretes par sommet
    nb_sommet = 0
    for line in fichier:
        nb_sommet += 1
        sommet = int(line.split()[0])  # donne le 1er élém de la ligne was int(line.split()[0])
        aretes = []
        for arete in line.split()[1:]:
            aretes.append(int(arete))
            nb_aretes += 1
        graphe[sommet] = aretes
        #  nb_aretes += len(aretes)
        Liste_arete.append(len(aretes))
    fichier.close()

    i = 100
    g = graphe
    Liste_coupe = []
    Coupe_Min(g,Liste_coupe)

    print("Nombres de sommets avant algorithme: ", nb_sommet)#len(list(graphe.keys())))
    print("Nombre d'aretes: ", nb_aretes/2)
    print("Coupe minimale: ", min(Liste_coupe))
    print("Coupe maximale: ", max(Liste_coupe))
    print("Coupe moyenne: ", statistics.mean(Liste_coupe))


Liste_coupe = []
main()








