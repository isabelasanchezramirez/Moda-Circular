from django.shortcuts import render, redirect
from .models import Usuario, Categoria, Testimonio, Alquiler

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
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'categorias/categorias.html', {'categorias': categorias})

def prendas(request):
    return render(request, 'prendas/prendas.html')

def sobreNosotros(request):
    return render(request, 'sobreNosotros/sobreNosotros.html')


def testimonios(request):
    testimonios = Testimonio.objects.all()  # Obtiene todos los testimonios
    return render(request, 'testimonios/testimonios.html', {'testimonios': testimonios})


def alquileres(request):
    alquileres = Alquiler.objects.all()  # Obtiene todos los alquileres
    return render(request, 'alquiler/alquileres.html', {'alquileres': alquileres})


