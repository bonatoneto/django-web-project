from django.contrib import admin
from django.urls import path
from django.utils import timezone
from django.shortcuts import render

from .models import Produto, Categoria, ItemCarrinho
from . import views

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(ItemCarrinho)


def produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'produto.html', {'produto': produto})


urlpatterns = [
    path('produto/<int:produto_id>/', views.produto, name='produto'),
]

# Código para popular o banco de dados (executar no shell do Django)
# from loja.models import Produto, Categoria
# from django.utils import timezone

# # Criar ou obter categorias
# categoria1, created = Categoria.objects.get_or_create(nome="Eletrônicos")
# categoria2, created = Categoria.objects.get_or_create(nome="Livros")

# # Criar produtos
# produtos = [
#     {
#         "nome": "Smartphone XYZ",
#         "preco": "1299.99",
#         "descricao": "Smartphone de última geração com câmera de alta resolução",
#         "categoria": categoria1
#     },
#     {
#         "nome": "Notebook ABC",
#         "preco": "3499.99",
#         "descricao": "Notebook potente para trabalho e jogos",
#         "categoria": categoria1
#     },
#     {
#         "nome": "Django para Iniciantes",
#         "preco": "89.90",
#         "descricao": "Aprenda Django do zero ao avançado",
#         "categoria": categoria2
#     }
# ]

# for p in produtos:
#     Produto.objects.create(
#         nome=p["nome"],
#         preco=p["preco"],
#         descricao=p["descricao"],
#         categoria=p["categoria"],
#         criado_em=timezone.now()
#     )

# print(f"{len(produtos)} produtos adicionados com sucesso!")
