from django.shortcuts import render, redirect
from .models import Prenda
from .models import Usuario

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

def prendas(request):
    return render(request, 'prendas/prendas.html')

def sobreNosotros(request):
    return render(request, 'sobreNosotros/sobreNosotros.html')





