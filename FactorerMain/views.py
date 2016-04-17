from django.views.generic import View
from django.shortcuts import render
from django.template.defaulttags import register
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

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    # @register.filter
    # def get_state(task):
    #     return task.

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user.id)[::-1]
        elements = Element.objects.filter(task__user=request.user.id)

        elements_dict = {}
        for element in elements:
            if element.task not in elements_dict.keys():
                elements_dict[element.task] = [(element.first_factor,
                                                element.second_factor)]
            else:
                elements_dict[element.task].append((element.first_factor,
                                                    element.second_factor))

        for task in tasks:
            if task not in elements_dict.keys():
                elements_dict[task] = ""

        context = {'tasks': tasks, 'elements_dict': elements_dict}

        return render(request, self.template_name, context)


class BruteforceView(LoggedInMixin, View):
    template_name = 'FactorerMain/algorithms/bruteforce.html'

    def get(self, request, *args, **kwargs):
        algorithm_form = AlgorithmInputForm()

        context = {'algorithm_form': algorithm_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        algorithm_form = AlgorithmInputForm(request.POST)
        if algorithm_form.is_valid():
            number = algorithm_form.cleaned_data['number']
            algorithm = Algorithm.objects.get(name="Brute Force")
            task = Task(number, request.user, algorithm)
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
            authenticated_user = authenticate(new_user.username,
                                              request.POST['password1'])
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
