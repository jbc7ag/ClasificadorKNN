
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'Puntos', PuntosApi.as_view(), name="puntos_endpoint"),
    url(r'(?P<x>[0-9]+)/(?P<y>[0-9]+)/(?P<k>[0-9]+)/$', ClassApi.as_view(), name="punto_endpoint"),

]