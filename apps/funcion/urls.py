from django.urls import path
from apps.funcion.views import FuncionCreate, FuncionDelete, FuncionList, FuncionUpdate,salas_ajax

urlpatterns=[
    path('registrar/', FuncionCreate.as_view(), name='registrar_funcion' ),
    path('editar/int:<pk>', FuncionUpdate.as_view(), name='editar_funcion' ),
    path('listar/', FuncionList.as_view(), name='listar_funcion' ),
    path('eliminar/int:<pk>', FuncionDelete.as_view(), name='eliminar_funcion' ),
    path('salas_ajax', salas_ajax, name='salas_ajax'),

    
]