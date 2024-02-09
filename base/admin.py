from django.contrib import admin
from .models import User, Field, Resource, AkiliRoom, Message, Event

# Register your models here.

admin.site.register(User)
admin.site.register(Field)
admin.site.register(Resource)
admin.site.register(AkiliRoom)
admin.site.register(Message)
admin.site.register(Event)
