from json import load, dump
from pyautogui import screenshot
from PIL import Image

"""
    {
    "screen" : [1270, 90, 400, 400],
    "grid_coords": [
        [[896, 347], [1108, 346], [1330, 347], [1547, 347]],
        [[890, 563], [1106, 563], [1330, 563], [1544, 563]],
        [[896, 779], [1106, 779], [1326, 779], [1543, 779]],
        [[890, 995], [1106, 995], [1323, 995], [1535, 995]]
    ],
    "time_wait" : 90,
    "time_wait_variance": 20,
    "file_name": "game",
    "path": "images/",
    "extention": ".jpg"
}
"""
def config_load(data_name):
    with open("config.json", "r") as file:
        try:
            return load(file)[data_name]
        except KeyError:
            print("ERROR : config.py | config_load : Key error")


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
    x = (x1 + x2 + x3 + x4) / 4
    y = (y1 + y2 + y3 + y4) / 4

    return x, y

def take_screen(file_name):
    screenshot(PATH+file_name+EXTENTION, SCREEN)

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

def update_coords(new_grid):
    # Charger le fichier JSON
    file_path = "config.json"
    with open(file_path, "r", encoding="utf-8") as file:
        data = load(file)

    data["grid_coords"] = new_grid

    # Sauvegarder les modifications en conservant l'indentation
    with open(file_path, "w", encoding="utf-8") as file:
        dump(data, file, ensure_ascii=False)


def configure_coords():
    t = [
        [[0, 0], [1108, 346], [1330, 347], [1547, 347]],
        [[890, 563], [1106, 563], [1330, 563], [1544, 563]],
        [[896, 779], [0, 0], [1326, 779], [1543, 779]],
        [[890, 995], [1106, 995], [1323, 995], [1535, 995]]
    ]
    update_coords(t)

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