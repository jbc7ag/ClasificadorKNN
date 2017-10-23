
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'Puntos', PuntosApi.as_view(), name="puntos_endpoint")

]