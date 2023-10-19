class Conjunto:
    def __init__(self):
        self.canibales = 0
        self.monjes = 0
        
    def total(self):
        return self.monjes + self.canibales
        
class Barco:
    def __init__(self):
        self.canibal = 0
        self.monje = 0
        self.lugar = 'izquierda'
    
    def mover(self):
        if self.lugar == 'derecha':
            self.lugar = 'izquierda'
        elif self.lugar == 'izquierda':
            self.lugar = 'derecha'
            
    def total(self):
        return self.monjes + self.canibales


class Estado:
    def __init__(self, izquierda, barco, derecha):
        self.izquierda = izquierda
        self.barco = barco
        self.derecha = derecha
        self.padre = None
        
    def padre(self, estadoPadre):
        self.padre = estadoPadre
        