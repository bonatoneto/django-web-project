from django.shortcuts import render, redirect
from .models import Produto, ItemCarrinho
from django.contrib import messages

def loja(request):
    produtos = Produto.objects.all()
    context = {
        'titulo': 'Nossa Loja',
        'produtos': produtos
    }
    return render(request, 'loja.html', context)

def carrinho(request):
    if not request.session.session_key:
        request.session.create()

    itens = ItemCarrinho.objects.filter(sessao_id=request.session.session_key)
    total = sum(item.subtotal() for item in itens)

    return render(request, 'carrinho.html', {
        'itens': itens,
        'total': total
    })

def adicionar_ao_carrinho(request, produto_id):
    if not request.session.session_key:
        request.session.create()

    produto = Produto.objects.get(id=produto_id)
    item, created = ItemCarrinho.objects.get_or_create(
        produto=produto,
        sessao_id=request.session.session_key
    )

    if not created:
        item.quantidade += 1
        item.save()

    messages.success(request, 'Produto adicionado ao carrinho!')
    return redirect('carrinho')

def remover_do_carrinho(request, produto_id):
    if not request.session.session_key:
        return redirect('carrinho')

    ItemCarrinho.objects.filter(
        produto_id=produto_id,
        sessao_id=request.session.session_key
    ).delete()

    return redirect('carrinho')

def produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render(request, 'produto.html', {'produto': produto})
