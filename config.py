from PIL import Image
from loader_config import config_load
from traitement import take_screen, read_data_file

PATH = config_load("path")
EXTENTION = config_load("extention")
SCREEN = config_load("screen")
NAME = "test"

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
    x = (x1 + x2 + x3 + x4) // 4
    y = (y1 + y2 + y3 + y4) // 4

    return x, y

def user_input(cases):
    choice = 0
    while choice < 1 or choice > len(cases):
        print("select your choice :")
        for i in range(len(cases)):
            print(f"{i+1} - {cases[i]}")
        try:
            choice = int(input())
        except ValueError:
            pass
        if choice < 1 or choice > len(cases):
            print(f"you must enter a number between 1 and {len(cases)}")
    return choice

def configure_coords():
    cells = read_data_file(NAME)
    for line in cells:
        print(center(line[0]), line[1])

if __name__ == "__main__":
    cases = ["take a screenshot", "configure_coords"]
    choice = user_input(cases)
    match choice:
        case 1:
            take_screen(NAME)
            Image.open(PATH+NAME+EXTENTION).show()
        case 2:
            configure_coords()
        case _:
            print("MissMatch")