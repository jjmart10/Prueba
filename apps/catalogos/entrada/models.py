from django.db import models


#Entradas
class entrada(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=200)
    estado = models.PositiveSmallIntegerField(default=1)
    class Meta:
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
