from django.forms import ModelForm, TextInput, NumberInput, DateInput
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'date']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите возраст'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            })
        }

