from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=250, blank=True)
    created_date = models.DateTimeField(auto_created=True, auto_now=True)
    description = models.TextField(blank=True)

    def __str__ (self) -> str:
        return f'{self.first_name} {self.last_name}'
