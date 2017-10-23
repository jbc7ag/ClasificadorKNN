from django.test import TestCase,Client

from django.urls import reverse
from rest_framework import status
from .models import Puntos
from .serializers import *
from .clasificador import ComonFunctions

import json


class PuntosTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_puntos(self):
        response =self.client.get(reverse("puntos_endpoint"))
        puntos = ComonFunctions.crearPuntos()
        serializer = PuntoSerializer(puntos, many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serializer.data,response.data)


    def test_get_kElements(self):
        response =self.client.get(reverse("puntos_endpoint"))
        puntos = ComonFunctions.crearPuntos()
        serializer = PuntoSerializer(puntos, many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serializer.data,response.data)