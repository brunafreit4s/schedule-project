from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import password_validation

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
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
    )    
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    # Validação do email:
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email
    
class RegisterUpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
        error_messages={
            'min_length': 'Nome inválido, verifique os valores informados!'
        }
    )    
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
        error_messages={
            'min_length': 'Nome inválido, verifique os valores informados!'
        }
    )
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label="Confirmação da Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password: 
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas são diferentes, verifique os valores informados!'),
                )                
        return super().clean()

    # Validação do email:
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email # email atual

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))

        return password1