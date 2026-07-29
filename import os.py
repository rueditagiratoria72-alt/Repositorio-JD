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

auto1 = automóvil("Toyota", "Corolla", 2020)
auto2 = automóvil("Honda", "Civic", 2021)
auto3 = automóvil("Ford", "Mustang", 2019)
auto4 = automóvil("Chevrolet", "Camaro", 2022)
auto5 = automóvil("Nissan", "Altima", 2020)

moto1 = motocicleta("Yamaha", "R1", 2021)
moto2 = motocicleta("Kawasaki", "Ninja", 2020)
moto3 = motocicleta("Ducati", "Panigale", 2022)
moto4 = motocicleta("Suzuki", "GSX-R1000", 2019)
moto5 = motocicleta("BMW", "S1000RR", 2021)

bicicleta1 = bicicleta("Trek", "Marlin 7", 2020)
bicicleta2 = bicicleta("Specialized", "Rockhopper", 2021)
bicicleta3 = bicicleta("Giant", "Talon 1", 2019)
bicicleta4 = bicicleta("Cannondale", "Trail 5", 2022)
bicicleta5 = bicicleta("Scott", "Aspect 930", 2020)        
