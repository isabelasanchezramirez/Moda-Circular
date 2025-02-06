from django.urls import path
from .views import lista_prendas, login, inicio, categorias
from . import views
urlpatterns = [
    path('', login, name='login'), 
    path('', views.inicio, name='inicio'), # La URL raíz apunta a la vista de login
    path('prendas/', lista_prendas, name='lista_prendas'),  # Cambia la URL para la lista de prendas
    #path('categorias/', lista_categorias, name='lista_categorias'),
    path('categorias/', categorias, name='categorias'),
    path('inicio/', inicio, name='inicio'),  # URL para la vista de inicio
]