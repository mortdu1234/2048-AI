"""gestion de l'image du jeu"""
import easyocr
from pyautogui import screenshot
from config import config_load

PATH = config_load("path")
EXTENTION = config_load("extention")
SCREEN = config_load("screen")
GRID_COORDS = config_load("grid_coords")


def take_screen(file_name):
    screenshot(PATH+file_name+EXTENTION, SCREEN)

def in_square(coord, square):
    """return if point in square

    Args:
        coord (tuple(int, int)): coord of a point
        square (tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]): corner of the square
    """
    # Extract the coordinates of the point.
    x, y = coord

    # Extract the coordinates of the four corners of the square.
    xa = min(square[0][0], square[1][0], square[2][0], square[3][0])
    ya = min(square[0][1], square[1][1], square[2][1], square[3][1])
    xb = max(square[0][0], square[1][0], square[2][0], square[3][0])
    yb = max(square[0][1], square[1][1], square[2][1], square[3][1])

    return xa <= x <= xb and ya <= y <= yb

def number_of(txt):
    value = ["I", "z", "3", "4", "s", "6", "7", "8", "x", "i", "x"]
    try:
        return value.index(txt[2]) + 1
    except ValueError:
        return "error" + txt[2]

def read_file(file_name):
    reader = easyocr.Reader(["fr"])
    element_read = reader.readtext(PATH+file_name+EXTENTION)
    cells = []
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # coordonnées des cases sur le screen (peu etre a modifier)
    
    # faire le trie dans les parties que l'on veut garder
    for elem in element_read:
        if "Lv" in elem[1]:
            cell = [elem[0], number_of(elem[1])]
            cells.append(cell)

    for line in range(len(GRID_COORDS)):
        for cols in range(len(GRID_COORDS[0])):
            for k in range(len(cells)):
                if in_square(GRID_COORDS[line][cols], cells[k][0]):
                    grid[line][cols] = cells[k][1]

    return grid

if __name__ == "__main__":
    file_name = "game"
    take_screen(file_name)
    grid = read_file(file_name)
    for line in grid:
        print(line)