from django.contrib.auth.forms import UserCreationForm
from .models import User


# class based user form for creating new user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']