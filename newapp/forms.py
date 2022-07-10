from .models import joint
from django.forms import ModelForm, TextInput, DateInput, MultipleChoiceField


class JointForm(ModelForm):
    class Meta:
        model = joint
        fields = ['title', 'line', 'locationweld',
                  'numberjoint', 'wayweld', 'dateweld', 'stamproot1', 'stamproot2', 'stampfilling1',
                  'stampfilling2']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'введите титул'
            }),
            'line': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'введите линию'
            }),
            'numberjoint': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите номер стыка'
            }),
        }
