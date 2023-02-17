#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
# Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
from math import pi
class Circulo:
    def __init__(self, centro,radio):
        self.centro = centro
        self.radio = radio
radio = float(input('Ingrese el radio del círculo: '))
area = pi * radio ** 2
print(f'El área del círculo es: {area}')