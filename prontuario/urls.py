from django.urls import path
from . import views # Importa as views do arquivo views.py deste app

urlpatterns = [
    # Caminho vazio para fazer referencia a /pronturario/ presente no urls do projeto
    path('', views.index) # Chamamos a view index mas não é para execução, apenas para referência, quando a URL for chamada a função index() será executada
]