from django import forms
from .models import ClienteFisica, ClienteJuridica, Fornecedor, Veiculo

class ClienteFModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Nascimento'].widget = forms.widgets.DateInput(
            attrs = {
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
        )
        self.fields['CPF'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['Telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['Celular'].widget.attrs.update({'class': 'mask-celular'})
        self.fields['Cep'].widget.attrs.update({'class': 'mask-cep'})

    class Meta:
        model = ClienteFisica
        fields = "__all__"


class ClienteJModelForm(forms.ModelForm):
    class Meta:
        model = ClienteJuridica
        fields = "__all__"


class FornecedorModelForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = "__all__"


class VeiculoModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Ano'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )

    class Meta:
        model = Veiculo
        fields = "__all__"


