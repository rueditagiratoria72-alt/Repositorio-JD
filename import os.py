import os
from abc import ABC

class Auto(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
