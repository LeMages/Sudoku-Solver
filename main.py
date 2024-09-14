grille = [[0, 0, 4, 7, 2, 9, 0, 0, 1],
 [0, 0, 0, 0, 4, 0, 0, 0, 0],
 [9, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 3, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 2, 5, 0, 0],
 [6, 3, 0, 0, 0, 0, 0, 0, 2],
 [7, 0, 1, 0, 3, 0, 0, 0, 5],
 [0, 0, 0, 0, 0, 7, 3, 0, 0],
 [8, 0, 0, 0, 0, 0, 0, 0, 0]]


# Affichage de la grille
def display():
    for i in range(0, 9):
        for j in range(0, 9):
            if grille[i][j] == 0:
                print(" . ", end="")
            else:
                print(f" {grille[i][j]} ", end="")
            if j % 3 == 2 and j != 9:
                print("|", end="")
        print("")
        if i % 3 == 2 and i != 9:
            print("_" * 30)


display()
