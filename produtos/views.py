from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'produtos/form.html', {'form': form})

def home(request):
    return render(request, 'produtos/home.html')