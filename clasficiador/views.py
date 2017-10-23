from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .models import Puntos
from .serializers import PuntoSerializer

from .clasificador import ComonFunctions

import requests
import json

# Create your views here.
class PuntosApi(APIView):

    def get(self, request):
        puntos= ComonFunctions.crearPuntos()
        serializer=PuntoSerializer(puntos, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ClassApi(APIView):

    def get(self, request, x, y, k):  #url http://localhost:8000/api/v1/clasificador/1/2/5/
        puntos= ComonFunctions.obtenerDistancia(x,y,k) #Regresa la lista de K elementos
        masComun=ComonFunctions.mas_comun(puntos)  #Nos regresa el elemento mas comun de la lista de los k elementos regresados
       # serializer=PuntoSerializer(masComun, many=True)
        return Response(masComun,status=status.HTTP_200_OK)





