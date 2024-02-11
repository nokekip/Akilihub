from django.shortcuts import render, redirect
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
    return render(request, 'register.html', context)


# home page
def index(request):
    return render(request, 'index.html')

