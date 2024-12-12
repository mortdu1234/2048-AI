"""gestion de l'image du jeu"""
import easyocr
from pyautogui import screenshot

PATH = "images/"
EXTENTION = ".jpg"

def take_screen(file_name):
    screenshot(PATH+file_name+EXTENTION, (0, 0, 1000, 1000))

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
    

def center(square):
    """return the coords x and y of the center of the square

    Args:
        square (tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]): corner of the square
    """
    # Extract the coordinates of the four corners of the square.
    x1, y1 = square[0]
    x2, y2 = square[1]
    x3, y3 = square[2]
    x4, y4 = square[3]

    # Calculate the average x and y coordinates of the four corners.
    x = (x1 + x2 + x3 + x4) / 4
    y = (y1 + y2 + y3 + y4) / 4

    return x, y

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
    grid_coord = [
        [(896, 347), (1108, 346), (1330, 347), (1547, 347)],
        [(890, 563), (1106, 563), (1330, 563), (1544, 563)],
        [(896, 779), (1106, 779), (1326, 779), (1543, 779)],
        [(890, 995), (1106, 995), (1323, 995), (1535, 995)]
    ]
    # faire le trie dans les parties que l'on veut garder
    for elem in element_read:
        if "Lv" in elem[1]:
            cell = [elem[0], number_of(elem[1])]
            cells.append(cell)

    for line in range(len(grid_coord)):
        for cols in range(len(grid_coord[0])):
            for k in range(len(cells)):
                if in_square(grid_coord[line][cols], cells[k][0]):
                    grid[line][cols] = cells[k][1]
    
    return grid

    
    

if __name__ == "__main__":
    file_name = "game"
    take_screen(file_name)
    grid = read_file(file_name)
    for line in grid:
        print(line)