from django.views.generic import View
from django.shortcuts import render

# Create your views here.

class IndexView(View):
    template_name = 'FactorerMain/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)