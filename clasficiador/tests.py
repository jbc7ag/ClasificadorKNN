from django.test import TestCase,Client

from django.urls import reverse
from rest_framework import status
from .models import Puntos
from .serializers import *
from .views import crearPuntos

import json




class PuntosTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_puntos(self):
        response =self.client.get(reverse("puntos_endpoint"))
        puntos = crearPuntos()
        serializer = PuntoSerializer(puntos, many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serializer.data,response.data)