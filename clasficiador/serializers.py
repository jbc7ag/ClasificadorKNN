from rest_framework import serializers
from .models import Puntos



class PuntoSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = Puntos
        fields = ['x','y','distancia','clase']