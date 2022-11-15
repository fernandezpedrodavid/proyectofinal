from django.contrib import admin
#
from .models import (
    Proyecto,
    Proyecto_Usuario
    ) 
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Proyecto_Usuario)