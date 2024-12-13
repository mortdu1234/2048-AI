from json import load

def config_load(data_name):
    with open("config.json", "r") as file:
        try:
            return load(file)[data_name]
        except KeyError:
            print("ERROR : config.py | config_load : Key error")
        

if __name__ == "__main__":
    a = config_load("patate")