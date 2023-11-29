from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*',}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Exemplo: Joana',
        })

        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Exemplo: Santos',
        })

        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Exemplo: (011) 91234-5678)',
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Exemplo: email@gmail.com',
        })

        self.fields['description'].widget.attrs.update({
            'placeholder': 'Descreva um texto...',
        })

    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
        # widgets = {
        #     'email': forms.EmailInput(attrs={
        #         'placeholder': 'E-mail'
        #     }),
        #     'description': forms.Textarea()            
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name