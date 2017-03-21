from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader


# Create your views here.


def index(request):
    return render(request, 'index.html', {'message': "ola"})
