from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.index, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    
    path('create-room/', views.createRoom, name='create-room'),
]
