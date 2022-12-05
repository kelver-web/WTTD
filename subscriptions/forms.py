from django import forms
from django.core.exceptions import ValidationError
from .models import Subscription


# def validate_cpf(value):
#     if not value.isdigit():
#         raise ValidationError('CPF deve conter apenas números.', 'digits')
#     if len(value) != 11:
#         raise ValidationError('CPF deve conter 11 números.', 'length')

class SubscriptionFormOld(forms.Form):
    name  = forms.CharField(label='Nome')
    #cpf   = forms.CharField(label='Cpf', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)
        # words = []
        # for w in name.split():
        #     words.append(w.capitalize())

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu telefone ou email.')
        return self.cleaned_data


class SubscriptionForm(forms.ModelForm):
    #cpf   = forms.CharField(label='Cpf', validators=[validate_cpf])
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    
    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu telefone ou email.')
        return self.cleaned_data

