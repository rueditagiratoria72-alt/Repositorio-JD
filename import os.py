import os
from abc import ABC
class vehículo(ABC):
    def __init__(self, marca, modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class automóvil(vehículo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def mostrar_info(self):
        return super().mostrar_info()

class motocicleta(vehículo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def mostrar_info(self):
        return super().mostrar_info()

class bicicleta(vehículo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)

    def mostrar_info(self):
        return super().mostrar_info()
        
