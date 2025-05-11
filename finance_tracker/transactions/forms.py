from django import forms
from .models import Transaction
from django.core.validators import MinValueValidator
from django.utils import timezone


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = kwargs.get('attrs', {})
        local_time = timezone.localtime(timezone.now())
        kwargs['attrs']['value'] = local_time.date()
        super().__init__(*args, **kwargs)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'type', 'category']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': CustomDateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].validators.append(MinValueValidator(0.01))
        self.fields['amount'].required = True
        self.fields['date'].required = True
        self.fields['type'].required = True
        self.fields['category'].required = True