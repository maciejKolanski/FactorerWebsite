from django.contrib import admin

# Register your models here.

from .models import UserData
from .models import Task
from .models import Algorithm

admin.site.register(UserData)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('number_to_factor', 'job_date', 'state', 'priority', 'result', 'user', 'algorithm')
    search_fields = ['user__username']
    list_filter = ('algorithm__name', 'user__username', 'state')

admin.site.register(Task, TaskAdmin)


class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Algorithm, AlgorithmAdmin)
