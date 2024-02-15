from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, AkiliRoom


# class based user form for creating new user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        
# form for akiliRoom
class AkiliRoomForm(ModelForm):
    class Meta:
        model = AkiliRoom
        fields = '__all__'
        exclude = ['owner', 'members']
        
# form for updating user
class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']