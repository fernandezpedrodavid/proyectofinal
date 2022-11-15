from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
#
from .models import (
    Proyecto,
    Proyecto_Usuario
) 
#
from .serializers import (
    ProyectoSerializer,
    ProyectoUpSerializer,
    ActiveUpSerializer,
    Proyecto_UsuarioSerializer
) 

# apis de backend para tabla Proyecto

class ProyectoListAPIView(ListAPIView):
    
    serializer_class = ProyectoSerializer
    
    def get_queryset(self):
        return Proyecto.objects.all()
    
    
class ProyectoCreateAPIView(CreateAPIView):
    
    serializer_class = ProyectoSerializer
    

class ProyectoUpApiView(RetrieveUpdateAPIView):
    
    serializer_class = ProyectoUpSerializer
    queryset = Proyecto.objects.all()
    

class ActiveUpAPIView(RetrieveUpdateAPIView):
    
    serializer_class = ActiveUpSerializer
    queryset = Proyecto.objects.all()
        
class ProyectoDestAPIView(DestroyAPIView):
    
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()
    

#Apis backend tabla Proyecto_Usuarios

class ProUsListAPIView(ListAPIView):
    
    serializer_class = Proyecto_UsuarioSerializer
    queryset = Proyecto_Usuario.objects.all() 
    
    
#Apis frontend para Proyecto

class ProyectoListView(ListView):
    template_name = "proyecto/lista.html"
    context_object_name = 'proyectos'
    
    def get_queryset(self):
        return Proyecto.objects.all()


class ProyectoCreateView(CreateView):
    template_name = "proyecto/crearpro.html"
    model = Proyecto
    fields = [
        'nombre',
        'is_active'
    ]
    success_url = '/lista/proyecto/'


class ProyectoUpdateView(UpdateView):
    template_name = "proyecto/mod-proyecto.html"
    model = Proyecto
    fields = [ 'nombre' ]
    success_url = '/lista/proyecto/'
    
class ActiveUpdateView(UpdateView):
    template_name = "proyecto/active-proyecto.html"
    model = Proyecto
    fields = [ 'is_active' ]
    success_url = '/lista/proyecto/'
    
class ProyectoDeleteView(DeleteView):
    template_name = "proyecto/delete-pro.html"
    model = Proyecto
    success_url = '/lista/proyecto/'
    

# Apis frontend Proyecto_Usuario


class Pro_UsListView(ListView):
    template_name = "proyecto_usuario/lista-pro-us.html"
    context_object_name = 'proyectousuario'
    
    def get_queryset(self):
        return Proyecto_Usuario.objects.all()
    
    
class ProUsCreateView(CreateView):
    template_name = "proyecto_usuario/crear-pro-us.html"
    model = Proyecto_Usuario
    fields = ('__all__')
    success_url = '/lista/proyecto_usuario/'

