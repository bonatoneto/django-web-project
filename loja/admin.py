from django.contrib import admin
from django.urls import path

from .models import Produto, Categoria
from . import views

admin.site.register(Produto)
admin.site.register(Categoria)


def produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'produto.html', {'produto': produto})


urlpatterns = [
    path('produto/<int:produto_id>/', views.produto, name='produto'),
]
