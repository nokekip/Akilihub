from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Field, AkiliRoom, Event, Message
from .forms import CreateUserForm, AkiliRoomForm

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
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            text=request.POST.get('text')
        )
        room.members.add(request.user)
        return redirect('room', pk=room.id)
    
    context = {'room': room,'threads': threads, 'members': members}
    return render(request, 'base/room.html', context)


# creating a room
def createRoom(request):
    form = AkiliRoomForm()
    fields = Field.objects.all()
    if request.method == 'POST':
        field_name = request.POST.get('field')
        field, created_at = Field.objects.get_or_create(name=field_name)
        
        AkiliRoom.objects.create(
            owner=request.user,
            field=field,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('home')
    
    context = {'form': form, 'fields': fields}
    return render(request, 'base/create-room.html', context)