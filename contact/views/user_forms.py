from django.shortcuts import render
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Usuário registrado com sucesso!')
            form.save()

    return render(
        request,
        'user/register.html',
        {
            'form': form
        }
    )