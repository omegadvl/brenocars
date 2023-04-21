from django.shortcuts import render
from django.contrib import messages
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .forms import ClienteFModelForm, ClienteJModelForm, FornecedorModelForm, VeiculoModelForm


@login_required()
def index(request):
    return render(request, 'registration/login.html')

def recuperar(request):
    return render(request, 'recuperar.html')

def menu(request):
    return render(request, 'menu.html')

def fisica(request):
    form = ClienteFModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente Cadastrado!')
            form = ClienteFModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar Veículo')
    else:
        form = ClienteFModelForm()
    context = {
        'form': form
    }
    return render(request, 'cadastroC_Fisica.html', context)

def juridica(request):
    form = ClienteJModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente Cadastrado!')
            form = ClienteJModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar Cliente')
    else:
        form = ClienteJModelForm()
    context = {
        'form': form
    }
    return render(request, 'cadastroC_Juridica.html', context)

def fornecedor(request):
    form = FornecedorModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor Cadastrado!')
            form = FornecedorModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar Fornecedor')
    else:
        form = FornecedorModelForm()

    context = {
        'form': form
    }
    return render(request, 'cadastro_Fornecedores.html', context)

def veiculos(request):
    form = VeiculoModelForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Veiculo Cadastrado!')
            form = VeiculoModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar Veículo')
    else:
        form = VeiculoModelForm()

    context = {
        'form': form
    }
    return render(request, 'cadastro_Veiculos.html', context)
