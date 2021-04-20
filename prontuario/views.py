from django.shortcuts import render
from django.http import HttpResponse # Importado

# Create your views here.
def index(request):
    return HttpResponse('Olá Mundo!')