# Pour chaque fonction une personne différente va :
# a. Programmer la fonction
# b. Créer le plan de tests
# c. Programmer les tests

"""
1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et les points d'attaques de l'autre et
qui retourne les points de vies restants après l'attaque.
"""

"""
2. Fonction qui reçoit une liste de legos et une couleur et qui reourne le pourcentage de blocs de cette couleur
"""

"""
3. Fonction qui reçoit une liste de legos et qui retourne il y a combien de blocs de chaque couleur en moyenne
"""

# Répartition des tâches :
"""                     a   b   c
Nom :Chris              1   2   3
Nom :Karl Irakoze       2   3   1
Nom :Fatoumata Maiga    3   1   2
"""


def points (vie,defense,attaque):
    vie_restant= (vie+defense) - attaque
    return vie_restant

if __name__=="__main__":
    vie = float(input("nombre de points de vie?: "))
    defense = float(input("nombre de points de defense?: "))
    attaque = float(input("nombre de points de attaque?: "))
    vie_restant = points(vie,defense,attaque,)
    print(f"le nombre de points de vies restants: {vie_restant}")


def ls_lego (couleur,pourcentage):
    couleur = ["bleu","rouge","jaune","vert"]
    pourcentage = ["15%","25%","20%","45%"]
    return

if __name__=="__main__":
    couleur = str(input("quelle est la couleur?: "))
    pourcentageindex(couleur)





