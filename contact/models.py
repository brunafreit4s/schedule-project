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

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=250, blank=True)
    created_date = models.DateTimeField(auto_created=True, auto_now=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='static/pictures/%Y/%m/')
    show = models.BooleanField(default=True)
    # on_delete=models.CASCADE = deleta em cascada
    # on_delete=models.SET_NULL = ao deletar a categoria, seta NULL no valor deletado
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, max_length=50)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__ (self) -> str:
        return f'{self.first_name} {self.last_name}'
