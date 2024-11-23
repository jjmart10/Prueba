from django.db import models
from apps.catalogos.departamento.models import Departamento

#MUICIPIOS
class   municipio(models.Model):
    codigo = models.CharField(verbose_name='Codigo', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'municipios'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
