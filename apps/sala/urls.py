from django.conf.urls import url, include
from django.urls import path
from apps.sala.views import  SalaCreate, SalaList,SalaUpdate, SalaDelete


urlpatterns= [
    path('registrar/', SalaCreate.as_view(), name='registrar_sala'),
    path('editar/int:<pk>', SalaUpdate.as_view(), name='editar_sala'),
    path('listar/', SalaList.as_view(), name='listar_sala'),
    path('eliminar/int:<pk>', SalaDelete.as_view(), name='eliminar_sala'),


]