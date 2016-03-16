from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import *
import operator

# Create your views here.

class IndexView(View):
    template_name = 'FactorerMain/index.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('number_to_factor')
        return render(request, self.template_name, {'tasks': tasks})