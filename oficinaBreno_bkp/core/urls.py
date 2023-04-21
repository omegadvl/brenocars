from django.urls import path
from .views import index, recuperar, menu, fisica, juridica, fornecedor, veiculos

urlpatterns = [
    path('', index, name='index'),
    path('recuperar.html', recuperar, name='recuperar'),
    path('menu.html', menu, name='menu'),
    path('cadastroC_Fisica.html', fisica, name='fisica'),
    path('cadastroC_Juridica.html', juridica, name='juridica'),
    path('cadastro_Fornecedores.html', fornecedor, name='fornecedor'),
    path('cadastro_Veiculos.html', veiculos, name='veiculos')
]
