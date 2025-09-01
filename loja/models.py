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

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    sessao_id = models.CharField(max_length=100)
    data_adicionado = models.DateTimeField(auto_created=True)

    def subtotal(self):
        return float(self.produto.preco) * self.quantidade
