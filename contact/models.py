from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__ (self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    first_name = models.CharField(max_length=100, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=100, verbose_name='Sobrenome')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(max_length=250, blank=True, verbose_name='E-mail')
    created_date = models.DateTimeField(auto_created=True, auto_now=True)
    description = models.TextField(blank=True, verbose_name='Descrição')
    picture = models.ImageField(blank=True, upload_to='static/pictures/%Y/%m/', verbose_name='Imagem')
    show = models.BooleanField(default=True, verbose_name='Mostrar')
    # on_delete=models.CASCADE = deleta em cascada
    # on_delete=models.SET_NULL = ao deletar a categoria, seta NULL no valor deletado
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, max_length=50, verbose_name='Categoria')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__ (self) -> str:
        return f'{self.first_name} {self.last_name}'
