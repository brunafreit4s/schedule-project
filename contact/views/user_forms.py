from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')            
            return redirect('user:login')

    return render(
        request,
        'user/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')
        
        messages.error(request, 'Login inválido')

    return render(
        request,
        'user/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

def user_update(request):
    form = RegisterUpdateUserForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'user/update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateUserForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'user/update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:login')