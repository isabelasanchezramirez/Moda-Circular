from django.shortcuts import render, redirect
from .models import Prenda
from .models import Usuario

def lista_prendas(request):
    prendas = Prenda.objects.all()  # Obtener todas las prendas
    return render(request, 'prendas/lista_prendas.html', {'prendas': prendas})
#def lista_categorias(request):
    #categorias = Categoria.objects.all()  # Obtener todas las categorías
    #return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            usuario = Usuario.objects.get(username=username, password=password)
            return redirect('inicio')  # Redirige a la vista de inicio si las credenciales son correctas
        except Usuario.DoesNotExist:
            error_message = "Usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')

def categorias(request):
    return render(request, 'categorias/categorias.html')