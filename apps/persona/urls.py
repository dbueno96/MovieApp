from django.conf.urls import url, include
from django.urls import path
from apps.persona.views import index, EmpleadoCreate, EmpleadoList,EmpleadoUpdate, EmpleadoDelete, PersonaCreate, PersonaUpdate, PersonaDelete, PersonaList, JefeCreate, JefeUpdate, JefeDelete, JefeList



urlpatterns = [
    path('', index, name='index'),
    path('registrar/', EmpleadoCreate.as_view(), name='registrar_empleado'),
    path('listar/', EmpleadoList.as_view(), name='listar_empleado'),
    path('editar/int:<pk>/', EmpleadoUpdate.as_view(), name='editar_empleado'),
    path('eliminar/int:<pk>/', EmpleadoDelete.as_view(), name='eliminar_empleado'),
    
    path('registrar_persona/', PersonaCreate.as_view(), name='registrar_persona'),
    path('listar_persona/', PersonaList.as_view(), name='listar_persona'),
    path('editar_persona/int:<pk>/', PersonaUpdate.as_view(), name='editar_persona'),
    path('eliminar_persona/int:<pk>/', PersonaDelete.as_view(), name='eliminar_persona'),

    path('registrar_jefe/', JefeCreate.as_view(), name='registrar_jefe'),
    path('listar_jefe/', JefeList.as_view(), name='listar_jefe'),
    path('editar_jefe/int:<pk>/', JefeUpdate.as_view(), name='editar_jefe'),
    path('eliminar_jefe/int:<pk>/', JefeDelete.as_view(), name='eliminar_jefe'),
    
]
