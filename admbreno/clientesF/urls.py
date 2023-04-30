from django.urls import path
from django.contrib.auth import views as auth_views
from .views import lista_clientes
from .views import criar_cliente
from .views import editar_cliente
from .views import excluir_cliente
from .views import (
    cadastro_veiculo,
    lista_veiculos,
    edita_veiculo,
    exclui_veiculo,
    criar_servico,
    cadastro_servico,
    lista_servicos,
    exclui_servico,
    edita_servico,
    cadastrar_fornecedor,
    fornecedores_list,
    fornecedor_edit,
    fornecedor_delete,
)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente'),
    path('editar_cliente/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('excluir_cliente/<int:pk>/', excluir_cliente, name='excluir_cliente'),
    path('lista_veiculos/', lista_veiculos, name='lista_veiculos'),
    path('cadastro_veiculo/', cadastro_veiculo, name='cadastro_veiculo'),
    path('edita_veiculo/<int:pk>/', edita_veiculo, name='edita_veiculo'),
    path('exclui_veiculo/<int:pk>/', exclui_veiculo, name='exclui_veiculo'),
    path('servico/novo/<int:veiculo_id>/', cadastro_servico, name='cadastro_servico'),
    path('lista_servicos/', lista_servicos, name='lista_servicos'),
    path('exclui_servico/<int:pk>/', exclui_servico, name='exclui_servico'),
    path('edita_servico/<int:pk>/', edita_servico, name='edita_servico'),
    path('../accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('cadastrar_fornecedor/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedores_list/', fornecedores_list, name='fornecedores_list'),
    path('fornecedor_edit/<int:pk>/', fornecedor_edit, name='fornecedor_edit'),
    path('fornecedor_delete/<int:pk>/', fornecedor_delete, name='fornecedor_delete'),

]
