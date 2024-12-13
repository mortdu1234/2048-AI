from traitement import take_screen, read_file
from ExpectedMax import best_choice, make_action
from math import log2, sqrt
from time import time, sleep
from config import config_load
from random import gauss

TIME_WAIT = config_load("time_wait")
DELTA_TIME_WAIT = config_load("time_wait_variance")
NAME = config_load("file_name")


def apply_log2(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                grid[i][j] = int(log2(grid[i][j]))
    return grid

def show_grid(grid1, grid2, action):
    """
    Affiche deux tableaux 2D l'un à côté de l'autre dans le terminal.

    :param grid1: Liste de listes (premier tableau 2D)
    :param grid2: Liste de listes (deuxième tableau 2D)
    """
    grid1 = apply_log2(grid1)
    grid2 = apply_log2(grid2)
    # Trouver la longueur maximale des tableaux
    print(f"         action make : {action}")
    print("   {:25}   {:25}".format("befor", "after"))
    longueur_max = max(len(grid1), len(grid2))

    # Étendre les tableaux pour qu'ils aient la même longueur (remplissage avec des listes vides)
    grid1 = grid1 + [[] for _ in range(longueur_max - len(grid1))]
    grid2 = grid2 + [[] for _ in range(longueur_max - len(grid2))]

    # Trouver la largeur maximale des lignes dans chaque tableau
    largeur_max1 = max((len(ligne) for ligne in grid1), default=0)
    largeur_max2 = max((len(ligne) for ligne in grid2), default=0)

    # Étendre chaque ligne pour qu'elle ait la même longueur
    grid1 = [ligne + [''] * (largeur_max1 - len(ligne)) for ligne in grid1]
    grid2 = [ligne + [''] * (largeur_max2 - len(ligne)) for ligne in grid2]

    # Afficher les tableaux côte à côte
    for ligne1, ligne2 in zip(grid1, grid2):
        ligne1_str = " ".join(f"{val:<3}" for val in ligne1)
        ligne2_str = " ".join(f"{val:<3}" for val in ligne2)
        print(f"{ligne1_str:<25} {ligne2_str}")


def main():
    # nombre de mouvements faisable en 24h = 1000
    for _ in range(1000):
        t1 = time()
        take_screen(file_name=NAME)
        grid_before = read_file(file_name=NAME)
        choice = best_choice(grid_before)
        grid_after = make_action(grid_before, choice)
        show_grid(grid_before, grid_after, choice)
        
        # gestion du temps d'attente
        time_to_wait = gauss(TIME_WAIT, sqrt(DELTA_TIME_WAIT))
        
        t2 = time()
        sleep(time_to_wait-(t2-t1))


if __name__ == "__main__":
    main()