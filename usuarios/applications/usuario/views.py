from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import(
    View,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import(
    FormView
)
#
from .forms import (
    UserRegisterForm,
    LoginForm,
)
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
    )
#
from .models import Usuario
#
from .serializers import (
    UsuarioSerializer,
    UsuarioUpSerializer,
    ActiveUpSerializer
    ) 

# Views para el backend

class UsuarioListAPIView(ListAPIView):
    
    serializer_class = UsuarioSerializer
    
    def get_queryset(self):
        return Usuario.objects.all()
    
    
class UsuarioCreateAPIView(CreateAPIView):
    
    serializer_class = UsuarioUpSerializer
    

class UsuarioUpApiView(RetrieveUpdateAPIView):
    
    serializer_class = UsuarioUpSerializer
    queryset = Usuario.objects.all()

class ActiveUpApiView(RetrieveUpdateAPIView):
    
    serializer_class = ActiveUpSerializer
    queryset = Usuario.objects.all()    
    
class UsuarioDestAPIView(DestroyAPIView):
    
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    

#Views frontend 

class RegistrarUsuario(FormView):
    template_name = 'usuario/registrar.html'
    form_class =  UserRegisterForm
    success_url = reverse_lazy('proyecto_app:lista-proyecto')
    
    def form_valid(self, form):
        
        Usuario.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            teléfono=form.cleaned_data['teléfono'],
            tipo_usuario =form.cleaned_data['tipo_usuario'],
        )  
        return super(RegistrarUsuario, self).form_valid(form)
    
    
class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('proyecto_app:lista-proyecto')
    
    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']   
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)
    
    
class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'usuario_app:login-usuario'
            )
        )    
    
    
class UsuarioListView(ListView):
    template_name = "usuario/lista-usuario.html"
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        return Usuario.objects.all()


class UsuarioUpdateView(UpdateView):
    template_name = "usuario/mod-usuario.html"
    model = Usuario
    fields = [
        'username',
        'password',
        'nombre',
        'apellido',
        'email',
        'tipo_usuario' 
    ]
    success_url = '/lista/usuario/'
    
class ActiveUsuarioView(UpdateView):
    template_name = "usuario/active-usuario.html"
    model = Usuario
    fields = [ 'is_active' ]
    success_url = '/lista/usuario/'
    
class UsuarioDeleteView(DeleteView):
    template_name = "usuario/delete-usuario.html"
    model = Usuario
    success_url = '/lista/usuario/'
