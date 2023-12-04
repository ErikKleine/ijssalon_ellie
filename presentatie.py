from helper import *

def presenteer(inkomsten):
    uitvoer = ""
    for key, value in inkomsten.items():
        uitvoer += f"{key} : {value}\n"
    uitvoer += f"==========================\ntotaal : {som(inkomsten)}"
    return uitvoer