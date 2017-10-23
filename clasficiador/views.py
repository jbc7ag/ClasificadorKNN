from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .models import Puntos
from .serializers import PuntoSerializer

import requests
import json

# Create your views here.
class PuntosApi(APIView):

    def get(self, request):
        puntos= crearPuntos()
        serializer=PuntoSerializer(puntos, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


def crearPuntos():

        animal1 = Puntos(x=2,y=1,distancia=4, clase="PERRO")
        animal2 = Puntos(x=2,y=1,distancia=4, clase="GATO")
        animal3 = Puntos(x=2,y=1,distancia=4, clase="PERRO")
        animal4 = Puntos(x=2,y=1,distancia=4, clase="GATO")
        animal5 = Puntos(x=2,y=1,distancia=4, clase="PERRO")
        animales = [animal1, animal2, animal3, animal4, animal5]
        return animales