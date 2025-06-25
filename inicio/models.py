from django.db import models

# Create your models here.
class meta: 
    verbose_name = "Alumnos"
    verbose_name_plural = "Alumnos"
    ordering = ["-creado"]

def __str__(self):
    return self.nombre
#Indica que se mostrara el nombre como valor en la tabla 
