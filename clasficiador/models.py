from django.db import models



TIPOANIMAL= (("PERRO" , "PERRO") , ("GATO" , "GATO"))


# Create your models here.
class Puntos(models.Model):
  #  x = models.DecimalField(decimal_places=2,max_digits=10)
  #  y = models.DecimalField(decimal_places=2,max_digits=10)
  #  distancia=models.DecimalField(decimal_places=2,max_digits=10)
  
    x = models.IntegerField()
    y = models.IntegerField()
    distancia=models.IntegerField()
    clase=models.CharField(choices=TIPOANIMAL,max_length=50)

    
  
 