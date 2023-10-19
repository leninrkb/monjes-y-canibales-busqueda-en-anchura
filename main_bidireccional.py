from queue import Queue
from clases import Conjunto, Barco, Estado
import copy
# uso una cola para busqueda en anchura


def subirIndividuoAlBarco(conjunto:Conjunto, barco:Barco):
    # sube un monje y un canibal al barco ssi esta vacio
    # si el barco tiene un canibal entonces sube un monje
    # si el barco tiene un monje entonces sube un canibal
    # muevo el barco al otro lado
    pass

def bajarIndividuoDelBarco(conjunto:Conjunto, barco:Barco):
    # si hay mas canibales que monjes baja un monje
    # si hay masn monjes que cabilaes baja un canibal
    # si hay igual numero de monjes y canibales baja cualquiera
    # muevo el barco al otro lado
    pass

def esObjetivo(estado:Estado):
    izquierda = estado.izquierda
    derecha = estado.derecha
    barco = estado.barco
    if izquierda.total() == 0 and barco.total() == 0 and derecha.total() == 0:
        return True
    return False


def seIntersecanEstados(estado1:Estado, estado2:Estado):
    if estado1.izquierda.total() == estado2.izquierda.total() and estado1.barco.total() == estado2.barco.total() and estado1.derecha.total() == estado2.derecha.total():
        return True
    return False
    
    
# arbol 1
izquierda = Conjunto()
izquierda.monjes = 3
izquierda.canibales = 3

derecha = Conjunto()
derecha.monjes = 0
derecha.canibales = 0

barco = Barco()

estadoInicial = Estado(izquierda, barco, derecha)

arbol1 = Queue()

arbol1.put(estadoInicial)

# arbol2 
izquierda_a2 = Conjunto()
izquierda_a2.monjes = 0
izquierda_a2.canibales = 0

derecha_a2 = Conjunto()
derecha_a2.monjes = 3
derecha_a2.canibales = 3

barco_a2 = Barco()

estadoInicial_a2 = Estado(izquierda, barco, derecha)

arbol2 = Queue()

arbol2.put(estadoInicial_a2)

solucion = None
while True:
    
    if not arbol1.empty():
        estadoActual1 = arbol1.get()
        # genero estados sucesores
        # agrego los nuevos estados a la  cola
        
    if not arbol2.empty():
        estadoActual2 = arbol2.get()
        # genero estados sucesores
        # agrego los nuevos estados a la  cola
    
    if seIntersecanEstados(estadoActual1, estadoActual2):
        break
    
# imprimo estado solucion 
    
