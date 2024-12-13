from pyautogui import write

def make_move(action):
    match action:
        case "haut":
            write("z")
        case "bas":
            write("s")
        case "gauche":
            write("q")
        case "droite":
            write("d")

if __name__ =="__main__":
    print("hello action")
    make_move("haut")