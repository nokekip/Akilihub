from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Field, AkiliRoom, Event
from .forms import CreateUserForm

# Create your views here.

# registering new user
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
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
    if request.user.is_authenticated:
        return redirect('home')
    
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
    return redirect('home')


# home page
def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    fields = Field.objects.all()
    rooms = AkiliRoom.objects.filter(
        Q(field__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    events = Event.objects.all()
    context = {'fields': fields, 'rooms': rooms, 'events': events}
    return render(request, 'base/index.html', context)


# single room page
def room(request, pk):
    room = AkiliRoom.objects.get(id=pk)
    threads = room.message_set.all()
    members = room.members.all()
    context = {'room': room,'threads': threads, 'members': members}
    return render(request, 'base/room.html', context)
