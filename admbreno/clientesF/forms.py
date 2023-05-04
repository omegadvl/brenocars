# No arquivo forms.py

from django import forms
from .models import Cliente
from .models import Veiculo
from .models import Servico
from .models import Fornecedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'profissao', 'telefone', 'celular', 'cep', 'endereco', 'cidade', 'estado', 'uf', 'email']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'ano', 'marca', 'modelo', 'cliente']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    
class ServicoForm(forms.ModelForm):
    descricao = forms.CharField(max_length=200)
    valor = forms.DecimalField(max_digits=7, decimal_places=2)
    data_entrega = forms.DateField(widget=forms.SelectDateWidget())
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.all())
    detalhes = forms.CharField(max_length=500, required=False)

    class Meta:
        model = Servico
        fields = ['cliente', 'veiculo', 'detalhes', 'descricao', 'valor', 'data_entrega']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()

        if 'cliente' in self.data:
            try:
                cliente_id = int(self.data.get('cliente'))
                self.fields['veiculo'].queryset = Veiculo.objects.filter(cliente_id=cliente_id).order_by('modelo')
            except (ValueError, TypeError):
                pass
        # elif self.instance.pk:
            # self.fields['veiculo'].queryset = self.instance.cliente.veiculo_set.order_by('modelo')

    def clean(self):
        cleaned_data = super().clean()
        veiculo = cleaned_data.get('veiculo')
        cliente = cleaned_data.get('cliente')

        if veiculo and cliente and veiculo.cliente != cliente:
            self.add_error('veiculo', 'O veículo não pertence ao cliente selecionado')

        return cleaned_data


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'nome_fantasia', 'cnpj', 'contato', 'segmento', 'telefone', 'celular', 'cep', 'endereco', 'cidade', 'estado', 'uf', 'email', 'site']
