import numpy as np

# Taille du Sudoku (9x9)
N = 9


# Vérifie si la valeur est valide dans la ligne
def est_valide_ligne(grille, ligne, valeur):
    return valeur not in grille[ligne]


# Vérifie si la valeur est valide dans la colonne
def est_valide_colonne(grille, colonne, valeur):
    return valeur not in [grille[i][colonne] for i in range(N)]


# Vérifie si la valeur est valide dans la région 3x3
def est_valide_region(grille, ligne, colonne, valeur):
    region_ligne = ligne - ligne % 3
    region_colonne = colonne - colonne % 3
    for i in range(3):
        for j in range(3):
            if grille[i + region_ligne][j + region_colonne] == valeur:
                return False
    return True


# Vérifie si la valeur est valide dans la case donnée (ligne, colonne)
def est_valide(grille, ligne, colonne, valeur):
    return (est_valide_ligne(grille, ligne, valeur) and
            est_valide_colonne(grille, colonne, valeur) and
            est_valide_region(grille, ligne, colonne, valeur))


# Trouve la prochaine case vide (notée par un 0)
def prochaine_case(grille):
    for i in range(N):
        for j in range(N):
            if grille[i][j] == 0:
                return i, j
    return None, None


# Algorithme de backtracking pour résoudre le Sudoku
def resoudre_sudoku(grille):
    ligne, colonne = prochaine_case(grille)

    # Si aucune case vide n'est trouvée, le sudoku est résolu
    if ligne is None:
        return True

    for valeur in range(1, N + 1):
        if est_valide(grille, ligne, colonne, valeur):
            grille[ligne][colonne] = valeur

            # Récurser pour essayer de résoudre la grille
            if resoudre_sudoku(grille):
                return True

            # Si l'ajout de la valeur ne mène pas à une solution, la retirer
            grille[ligne][colonne] = 0

    return False


# Exemple d'utilisation
grille = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]


# Résoudre le Sudoku
if resoudre_sudoku(grille):
    print(np.array(grille))
else:
    print("Aucune solution n'a été trouvée.")
