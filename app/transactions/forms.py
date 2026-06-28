from django import forms
from .models import Transaction

BS_INPUT = 'form-control'


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'category', 'description', 'date']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'amount': forms.NumberInput(attrs={
                'class': BS_INPUT,
                'step': '0.01',
                'min': '0',
                'placeholder': '0.00',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'description': forms.Textarea(attrs={
                'class': BS_INPUT,
                'rows': 3,
                'placeholder': 'Opcional — descripción de la transacción',
            }),
            'date': forms.DateInput(attrs={
                'class': BS_INPUT,
                'type': 'date',
            }),
        }
