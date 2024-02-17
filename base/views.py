from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Field, AkiliRoom, Event, Message, User
from .forms import CreateUserForm, AkiliRoomForm, UpdateUserForm

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
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('home')
        else:
            # messages.info(request, 'Invalid registration details')
            for error in form.errors:
                messages.error(request, form.errors[error])
            
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
    fields = Field.objects.all()[0:5]
    rooms = AkiliRoom.objects.filter(
        Q(field__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    events = Event.objects.all()
    context = {'fields': fields, 'rooms': rooms, 'events': events}
    return render(request, 'base/index.html', context)

# Fields page
def fields(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    fields = Field.objects.filter(name__icontains=q)
    context = {'fields': fields}
    return render(request, 'base/fields.html', context)


# single room page
@login_required(login_url='login')
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


# user profile
@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.akiliroom_set.all()
    room_messages = user.message_set.all()
    fields = Field.objects.all()
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'fields': fields}
    return render(request, 'base/profile.html', context)


# creating a room
@login_required(login_url='login')
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

# Update room details
@login_required(login_url='login')
def updateRoom(request, pk):
    room = AkiliRoom.objects.get(id=pk)
    form = AkiliRoomForm(request.POST or None, instance=room)
    fields = Field.objects.all()
    
    if request.method == 'POST':
        field_name = request.POST.get('field')
        field, created_at = Field.objects.get_or_create(name=field_name)
        room.name = request.POST.get('name')
        room.field = field
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    
    context = {'form': form, 'fields': fields, 'room': room}
    return render(request, 'base/create-room.html', context)


# delete room
@login_required(login_url='login')
def deleteRoom(request, pk):
    room = AkiliRoom.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room}
    return render(request, 'base/delete.html', context)

# delete message
@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context = {'obj': message}
    return render(request, 'base/delete.html', context)

# update user profile
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    
    context = {'form': form}
    return render(request, 'base/edit-user.html', context)

def events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'base/activity.html', context)
