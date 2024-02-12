from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Create your views here.

# registering new user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/signup.html', context)


# login user
def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = user.object.get(email=email)
        except:
            messages.error(request, 'User does not exist!')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'base/login.html')


# logout user
def logoutUser(request):
    logout(request)
    return redirect('base/home')


# home page
def index(request):
    return render(request, 'base/index.html')

