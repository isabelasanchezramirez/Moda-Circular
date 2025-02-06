from django.urls import path
from .views import prendas, login, inicio, categorias, sobreNosotros
from . import views
urlpatterns = [
    path('', login, name='login'), 
    path('', views.inicio, name='inicio'), # La URL raíz apunta a la vista de login
    path('prendas/', prendas, name='prendas'),  # Cambia la URL para la lista de prendas
    path('categorias/', categorias, name='categorias'),
    path('sobreNosotros/',sobreNosotros, name='sobreNosotros'),
    path('inicio/', inicio, name='inicio'),  # URL para la vista de inicio
]