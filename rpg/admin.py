from django.contrib import admin
from .models import Job
from .models import Item
from .models import Character

# Register your models here.
admin.site.register(Job)
admin.site.register(Item)
admin.site.register(Character)