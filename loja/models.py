from django.db import models
from django.utils import timezone

class Categoria(models.Model):
  nome = models.CharField(max_length=200)

  def __str__(self):
    return self.nome

class Produto(models.Model):
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  nome = models.CharField(max_length=200)
  preco = models.TextField()
  descricao = models.TextField()
  criado_em = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.nome
