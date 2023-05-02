from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente, Veiculo
from .forms import ClienteForm
from .forms import VeiculoForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Servico
from .models import Fornecedor
from .forms import ServicoForm
from .forms import FornecedorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, '../templates/clientesF/index.html')


#Criar clientes
@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, '../templates/clientesF/criar_cliente.html', {'form': form})  


#Listar clientes
@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, '../templates/clientesF/lista_clientes.html', {'clientes': clientes})


#Editar Clientes
@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, '../templates/clientesF/editar_cliente.html', {'form': form})


# excluir cliente
@login_required
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'excluir_cliente.html', {'cliente': cliente})


#veiculos
@login_required
def cadastro_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm()

    return render(request, 'clientesF/veiculo_form.html', {'form': form})

@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'clientesF/veiculo_list.html', {'veiculos': veiculos})

@login_required
def exclui_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    
    if request.method == 'POST':
        veiculo.delete()
        return redirect('lista_veiculos')
    return render(request, 'clientesF/excluir_veiculo.html', {'veiculo': veiculo})

@login_required
def edita_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    cliente_pk = veiculo.cliente.pk
    form = VeiculoForm(request.POST or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect('lista_veiculos')
    return render(request, 'clientesF/veiculo_form.html', {'form': form, 'pk': cliente_pk})


## Servico
@login_required
def criar_servico(request):
    form = ServicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_servicos')
    return render(request, 'clientesF/servico_form.html', {'form': form})
@login_required
def cadastro_servico(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
    cliente = veiculo.cliente

    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.veiculo = veiculo
            servico.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm(initial={'cliente': cliente, 'veiculo': veiculo})

    context = {'form': form}
    return render(request, 'clientesF/servico_form.html', context)

@login_required 
def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'clientesF/servico_list.html', {'servicos': servicos})

@login_required
def exclui_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    
    if request.method == 'POST':
        servico.delete()
        return redirect('lista_servicos')
    return render(request, 'clientesF/servico_list.html', {'servico': servico})

@login_required
def edita_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('lista_servicos')
    else:
        form = ServicoForm(instance=servico)
    
    return render(request, 'clientesF/edicao_servico.html', {'form': form, 'servico': servico})


## Fornecedor
@login_required   
def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores_list')
    else:
        form = FornecedorForm()
    return render(request, 'clientesF/fornecedor_form.html', {'form': form})

@login_required 
def fornecedores_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'clientesF/fornecedores_list.html', {'fornecedores': fornecedores})

@login_required   
def fornecedor_edit(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return redirect('fornecedores_list')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'clientesF/fornecedor_edit.html', {'form': form})

@login_required 
def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedores_list')
    return render(request, 'fornecedor_delete.html', {'fornecedor': fornecedor})
