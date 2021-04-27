import PySimpleGUI as sg 
from src.windows import game
def start():
    window = loop()
    window.close()

def loop():
    player = {"name":"Maria"}
    board_data = [[" "] * 8 for _i in range(8) ]
    window = game.build(player, board_data)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
    return window