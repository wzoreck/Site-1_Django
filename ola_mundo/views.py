from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apresentar(request):
    return render(request, 'ola_mundo/index.html') # Vai renderizar o HTML presente no diretório templates
