from django.db import models

# Create your models here.


    
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(null=True, blank=True)
    NIF = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo = models.TextField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    valor = models.FloatField(null=True, blank=True)
    data_submissao = models.DateField(null=True, blank=True)
    estado = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.tipo + ' - ' + self.empresa_id.nome