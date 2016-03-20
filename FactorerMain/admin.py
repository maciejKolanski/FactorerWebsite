from django.contrib import admin

# Register your models here.

from .models import UserData
from .models import Task
from .models import Algorithm
from .models import Element

admin.site.register(UserData)
admin.site.register(Task)
admin.site.register(Algorithm)
admin.site.register(Element)