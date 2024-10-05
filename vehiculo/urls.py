from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('add/', agregar_vehiculo, name='agregar_vehiculo'),
    path('listar/', listar_vehiculos, name='listar_vehiculos'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('registro/', registro, name='registro'),

]
