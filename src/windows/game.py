import PySimpleGUI as sg
import time

def time_as_int():
    return int(round(time.time()*100))

def build(player, board_data):

    layout = [
        [sg.Text("Jugador: " + player["name"], key="-P1-", text_color="darkblue")]
    ]

    for y in range(8):
        layout += [
            [
                sg.Button(board_data[x][y], size=(4,2), key=f"cell-{x}-{y}")
                for x in range(8)
            ]
        ]
    board = sg.Window("MemPy").Layout(layout)
    return board
    