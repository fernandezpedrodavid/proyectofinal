from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
#


class Usuario(AbstractBaseUser, PermissionsMixin):
    
    Tipo_Usuario = [
        (0,'Superusuario'),
        (1, 'Admin'),
    ]
    
    username = models.CharField( max_length=10, unique=True)
    password = models.CharField('Password', max_length=100)
    nombre = models.CharField('Nombre', max_length=30, blank=True)
    apellido = models.CharField('Apellido', max_length=30, blank=True)
    teléfono = models.IntegerField(null=True)
    email = models.EmailField(("Email"), max_length=100)
    tipo_usuario = models.IntegerField(choices=Tipo_Usuario, null=True)
    #para especificar si puede acceder a la pag de administrador de django
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email',]
    
    objects = UserManager()
    
    def get_short_name(self):
        return self.username + '-' + self.nombre
        