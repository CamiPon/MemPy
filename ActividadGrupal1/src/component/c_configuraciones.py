from src.windows import v_configuraciones
from src.model.configuracion import configuracion
import json
import PySimpleGUI as sg


def start():
    window = loop()
    window.close()

def loop():
    username = "Carla"
    conf = configuracion(username)
    window = v_configuraciones.build(conf.buscarConfig())
    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break
        
    return window