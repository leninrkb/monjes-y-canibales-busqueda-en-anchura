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


izquierda = Conjunto()
izquierda.monjes = 3
izquierda.canibales = 3

derecha = Conjunto()
derecha.monjes = 0
derecha.canibales = 0

barco = Barco()

estadoInicial = Estado(izquierda, barco, derecha)

cola = Queue()

cola.put(estadoInicial)

solucion = None
while not cola.empty():
    estadoActual = cola.get()
    if esObjetivo(estadoActual):
        solucion = estadoActual
        break
    # genero estados sucesores
    # agrego los nuevos estados a la  cola
    
# imprimo estado solucion 
    
