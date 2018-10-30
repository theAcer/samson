from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(self, request, **kwargs):
    return render(request, 'index.html', context=None)
