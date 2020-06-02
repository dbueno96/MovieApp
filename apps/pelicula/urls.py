from django.conf.urls import url, include
from django.urls import path

from apps.pelicula.views import index
from apps.pelicula.views import PeliculaList, PeliculaCreate, PeliculaUpdate, PeliculaDelete

urlpatterns = [
    path('', index, name='index'),
    path('registrar/', PeliculaCreate.as_view(), name='registrar_pelicula'),
    path('listar/', PeliculaList.as_view(), name='listar_pelicula'),
    path('editar/int:<pk>', PeliculaUpdate.as_view(), name='editar_pelicula'),
    path('eliminar/<int:pk>/', PeliculaDelete.as_view(), name='eliminar_pelicula'),
    
]
