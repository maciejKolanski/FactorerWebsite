from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .mixin import LoggedInMixin
from .forms import *

# Create your views here.


class IndexView(LoggedInMixin, View):
    template_name = 'FactorerMain/index.html'

    @staticmethod
    def data_to_render():
        tasks = Task.objects.order_by('-id')[:10]
        users = User.objects.order_by('username')
        return {'tasks': tasks, 'users': users}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, IndexView.data_to_render())


class UserView(LoggedInMixin, View):
    template_name = 'FactorerMain/userview.html'

    def get(self, request, *args, **kwargs):        
        tasks = Task.objects.filter(user=request.user.id)[::-1]
        elements = Element.objects.filter(task__user=request.user.id)

        return render(request, self.template_name, {'tasks': tasks, 'elements': elements})


class BruteforceView(LoggedInMixin, View):
    template_name = 'FactorerMain/algorithms/bruteforce.html'

    def get(self, request, *args, **kwargs):
        algorithm_form = AlgorithmInputForm()
        return render(request, self.template_name, {'algorithm_form': algorithm_form})

    def post(self, request, *args, **kwargs):
        algorithm_form = AlgorithmInputForm(request.POST)
        if algorithm_form.is_valid():
            number = algorithm_form.cleaned_data['number']
            algorithm = Algorithm.objects.get(name="Brute Force")#TODO something with hardoced name
            task = Task(number_to_factor=number, user=request.user, algorithm=algorithm)
            task.save()
            return HttpResponseRedirect("/")
        return HttpResponse("Failed to get brute force number")


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