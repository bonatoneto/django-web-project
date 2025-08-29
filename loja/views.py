from django.shortcuts import render

# Create your views here.
def loja(request):

    context = {
        'titulo': ''
    }

    return render(request, 'loja.html', context)

def carrinho(request):
    return render(request, 'base.html', {})
