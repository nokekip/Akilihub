from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('', views.index, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('fields/', views.fields, name='fields'),
    path('events/', views.events, name='events'),
    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),
    
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    
    path('upate-user/', views.updateUser, name='update-user'),
]
