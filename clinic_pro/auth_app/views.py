from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def register_form(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user_urls')
    template_name = 'auth_app/register.html'
    context = {'form': form}
    return render(request, template_name, context)

def login_view(request):
    template_name = 'auth_app/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_urls')
    return render(request, template_name)

def logout_view(request):
    logout(request)
    return redirect('login_user_urls')

