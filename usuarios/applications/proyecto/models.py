from http.client import PROXY_AUTHENTICATION_REQUIRED
from django.db import models
#
from applications.usuario.models import Usuario


# model para tabla Proyecto
class Proyecto(models.Model):
    nombre = models.CharField('Proyecto', max_length=50)
    is_active = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return self.nombre
    

#model para tabla Proyecto_Usuario    
class Proyecto_Usuario(models.Model):
    proyecto_id= models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE
    )
    usuario_id = models.ForeignKey( 
        Usuario,
        on_delete=models.CASCADE, 
        null=True
    )
    is_active = models.BooleanField(default=True)
    
   #objects = ProyectoUsuario
    
    def __str__(self):
        return  str(self.id) 
    
    