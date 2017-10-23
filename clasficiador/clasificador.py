
from .models import Puntos
from .Knn import Knn

import collections


class ComonFunctions:

    def obtenerDistancia(x,y,k):

            animal1 = Puntos(x=x,y=y,distancia=0,clase="")     
            animales = ComonFunctions.crearPuntos()
            lista=  Knn.setObjectsDistance(animales, animal1)
            lista=  ComonFunctions.por_elementos_cercanos(lista, k)
            return lista


    def crearPuntos():
            animal1 = Puntos(x=2,y=1,distancia=4, clase="PERRO")
            animal2 = Puntos(x=2,y=1,distancia=4, clase="GATO")
            animal3 = Puntos(x=2,y=1,distancia=4, clase="PERRO")
            animal4 = Puntos(x=2,y=1,distancia=4, clase="GATO")
            animal5 = Puntos(x=2,y=1,distancia=4, clase="PERRO")
            animales = [animal1, animal2, animal3, animal4, animal5]
            return animales


    def por_elementos_cercanos(animales, elementos):
        lista = sorted(animales, key=lambda animal:int(animal.distancia))
        return  lista[:int(elementos)]

    def mas_comun(animales):
        lista = []
        for animal  in animales:
            lista.append(animal.clase)
        c = collections.Counter(lista)
        return (c.most_common(1))


    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                  self.x,
                                  self.y,
                                  self.distancia,
                                  self.clase
                                  )
