from django.urls import path, re_path
# 
from. import (
    views,
)
app_name = 'usuario_app'

urlpatterns = [
    path(
        'api/list/usuario',
        views.UsuarioListAPIView.as_view(),
    ),
      path(
        'api/usuario/create/',
        views.UsuarioCreateAPIView.as_view(),
    ),
    path(
        'api/usuario/update/<pk>/',
        views.UsuarioUpApiView.as_view(),
    ),
    path(
        'api/active/update/<pk>/',
        views.ActiveUpApiView.as_view(),
    ),
    path(
        'api/usuario/delete/<pk>/',
        views.UsuarioDestAPIView.as_view(),
    ),
#Urls frontend 
    path(
        'registrar/usuario/',
        views.RegistrarUsuario.as_view(),
        name='registre-usuario'
    ),
    path(
        'login/',
        views.Login.as_view(),
        name='login-usuario'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='logout-usuario'
    ),
    path(
        'lista/usuario/',
        views.UsuarioListView.as_view(),
        name='lista-usuario'
    ),
    path(
        'cambiar/usuario/<pk>/',
        views.UsuarioUpdateView.as_view(),
        name='cambiar-usuario'
    ),
    path(
        'activar/usuario/<pk>/',
        views.ActiveUsuarioView.as_view(),
        name='active-usuario'
    ),
    path(
        'eliminar/usuario/<pk>/',
        views.UsuarioDeleteView.as_view(),
        name='elimine-usuario'
    ),
]
