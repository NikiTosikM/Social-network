from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, RegisterForm, UserProfile

from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(reverse('user:account'), request=request)
        
        else:
            return render(request, 'User/login.html', {'form': form})
    else:
        form = LoginForm()
        
        return render(request, 'User/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse('user:account'))
        
        else:
            return render(request, 'User/register.html', {'form': form})
        
    else:
        form = RegisterForm()

        return render(request, 'User/register.html', {'form': form})
    

def account_user_view(request):
    form = UserProfile(instance=request.user)

    return render(request, 'User/account.html', {'form': form})