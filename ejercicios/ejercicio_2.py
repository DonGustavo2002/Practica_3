# 1. Cree una clase Punto que represente un punto en el plano cartesiano.
# 2. A la clase del punto anterior, defínale los siguientes métodos:

class Punto:
    def __int__(self,x,y):
        self.x = x
        self.y = y
    def usarx(self):
        return self.x
    def usary(self):
        return self.y
    def ubicarx(self):
        self.x = self.x + 1
    def ubicary(self):
        self.y = self.y + 1


    def mostrarPunto(self):
        print("/nX"+ str(self.usarx())+ "/nY:" +str(self.usary()) )
x = input("")
y = input("")
p = coordenada(x,y)
p.vercoordenada()
