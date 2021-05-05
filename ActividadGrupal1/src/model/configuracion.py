
import json
import os
class configuracion():

    def __init__(self,username,textos = "", cant_casillas = "8x8", tiempo = 120, estilo = "Predeterminado", tipo_elementos = "Ambos", ayudas = "No"):
        self.username = username,
        self.textos = textos,
        self.cant_casillas = cant_casillas,
        self.tiempo = tiempo,
        self.estilo = estilo,
        self.tipo_elementos = tipo_elementos,
        self.ayudas = ayudas,
        
    def guardarJson(self):
        try:
            with open("archivos"+ os.sep +"arc_configuracion.json", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion= []
        with open("Archivos"+ os.sep +"arc_configuracion.json", "w", encoding="utf8") as file:
            data = {
                self.username : {
                "textos" : self.textos,
                "cantidad de casillas" : self.cant_casillas,
                "tiempo maximo" : self.tiempo,
                "estilo" : self.estilo,
                "tipo elementos" : self.tipo_elementos,
                "ayudas" : self.ayudas,
                }
            }
            data_configuracion.append(data)
            json.dump(data_configuracion,file, indent=4, ensure_ascii=False)

    def buscarConfig(self):
        try:
            with open("Archivos"+ os.sep +"arc_configuracion.json", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion = []
        for aux in data_configuracion:
            if self.username in aux:
                self = configuracion(
                    self.username,
                    aux[self.username]["textos"],
                    aux[self.username]["cant_casillas"],
                    aux[self.username]["tiempo"],
                    aux[self.username]["estilo"],
                    aux[self.username]["tipo elementos"],
                    aux[self.username]["ayudas"]
                    )
        return self