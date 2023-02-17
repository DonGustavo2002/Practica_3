#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
class Rectangulo:
    def __init__(self,ancho,alto):
        self.ancho= ancho
        self.alto= alto

    def area(self):
        area=self.alto * self.ancho
        return area

    def perimetro(self):
        perimetro=(self.alto*2)+(self.ancho*2)
        return perimetro

r1=Rectangulo(4,2)
area=r1.area()
perimetro=r1.perimetro()
print("El area es:",area)
print("El perimetro es:",perimetro)