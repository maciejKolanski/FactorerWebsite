from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import *
from .mixin import LoggedInMixin
import operator

# Create your views here.

class IndexView(LoggedInMixin, View):
    template_name = 'FactorerMain/index.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('number_to_factor')
        users = UserData.objects.order_by('login')
        return render(request, self.template_name, {'tasks': tasks, 'users': users})


class AboutView(LoggedInMixin, View):
    template_name = 'FactorerMain/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class CreatorsView(LoggedInMixin, View):
    template_name = 'FactorerMain/creators.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})