from django.shortcuts import render
from django.views.generic import FormView, TemplateView

# Create your views here.
from django.http import HttpResponse



def index(self, request, **kwargs):
    return render(request, 'index.html', context=None)


class HomeView(TemplateView):
    template_name = 'index.html'
