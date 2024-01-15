from datetime import datetime

class Status():
    articulo: str 
    cliente: str
    n_articulo: str
    color: str 
    peso: float 
    metros: float 
    n_rollo: int 
    rendimiento: float 
    operario: str 
    ancho: float 
    last_update: str

    def dict(self):
        return self.__dict__()