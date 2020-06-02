from django.conf.urls import url, include
from django.urls import path
from apps.teatro.views import  TeatroCreate, TeatroList,TeatroUpdate, TeatroDelete


urlpatterns= [
    path('registrar/', TeatroCreate.as_view(), name='registrar_teatro'),
    path('editar/int:<pk>', TeatroUpdate.as_view(), name='editar_teatro'),
    path('listar/', TeatroList.as_view(), name='listar_teatro'),
    path('eliminar/int:<pk>', TeatroDelete.as_view(), name='eliminar_teatro'),

]