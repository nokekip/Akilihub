from django.contrib import admin
from .models import User, Field, Resource, AkiliRoom

# Register your models here.

admin.site.register(User)
admin.site.register(Field)
admin.site.register(Resource)
admin.site.register(AkiliRoom)
