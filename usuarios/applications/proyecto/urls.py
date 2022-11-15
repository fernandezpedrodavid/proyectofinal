from django.urls import path, re_path
# 
from. import (
    views,
)
app_name = 'proyecto_app'

# URLS para el backend Proyecto

urlpatterns = [
    path(
        'api/list/proyecto',
        views.ProyectoListAPIView.as_view(),
    ),
    path(
        'api/proyecto/create/',
        views.ProyectoCreateAPIView.as_view(),
    ),
    path(
        'api/proyecto/update/<pk>/',
        views.ProyectoUpApiView.as_view(),
    ),
    path(
        'api/active/update/<pk>/',
        views.ActiveUpAPIView.as_view(),
    ),
    path(
        'api/proyecto/delete/<pk>/',
        views.ProyectoDestAPIView.as_view(),
    ),
#urls backend Proyecto_usuario
    path(
        'api/list/proyecto_usuario',
        views.ProUsListAPIView.as_view(),
    ),
#Urls frontend Proyecto
    path(
        'lista/proyecto/',
        views.ProyectoListView.as_view(),
        name='lista-proyecto'
    ),
    path(
        'crear/proyecto/',
        views.ProyectoCreateView.as_view(),
        name='nuevo-proyecto'
    ),
    path(
        'cambiar/nombre/<pk>/',
        views.ProyectoUpdateView.as_view(),
        name='nuevo-nombre'
    ),
    path(
        'activar/proyecto/<pk>/',
        views.ActiveUpdateView.as_view(),
        name='active-proyecto'
    ),
    path(
        'eliminar/proyecto/<pk>/',
        views.ProyectoDeleteView.as_view(),
        name='elimine-proyecto'
    ),
#Urls para Proyecto_Usuario
    path(
        'lista/proyecto_usuario/',
        views.Pro_UsListView.as_view(),
        name='lista-proyecto-usuario'
    ),
    path(
        'crear/proyecto_usuario/',
        views.ProUsCreateView.as_view(),
        name='crear-proyecto-usuario'
    ),
]





