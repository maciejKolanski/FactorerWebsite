from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout,  login
from django.http import HttpResponseRedirect
from django import forms
from .models import *
from .mixin import LoggedInMixin
import operator

# Create your views here.

class IndexView(LoggedInMixin, View):
    template_name = 'FactorerMain/index.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('number_to_factor')
        users = User.objects.order_by('username')
        return render(request, self.template_name, {'tasks': tasks, 'users': users})


class AboutView(LoggedInMixin, View):
    template_name = 'FactorerMain/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class CreatorsView(LoggedInMixin, View):
    template_name = 'FactorerMain/creators.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect("/success_register")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

class SuccessRegisterView(LoggedInMixin, View):
    template_name = 'FactorerMain/success_register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})