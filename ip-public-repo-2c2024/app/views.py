# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Favourite



def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    # Filtrar personajes si hay un input en el request
    
    characters_list = services.getAllImages() # Llamada a la función de services.py
    
   

    # Enviar los datos al template home.html
    return render(request, 'home.html', {
        'images': characters_list,  # Lista de personajes obtenidos de la API
        'favorites': []     # Lista de favoritos del usuario
    })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py
    # y luego renderiza el template.
    if (search_msg != ''):
        images = services.getAllImages(search_msg) # llama a la funcion de obtener todas las imagenes usando el input del cuadro de busqueda
        # llama a la lista de favoritos para que se muestren correctamente cuando utilizamos la barra de busqueda
        favourite_list = services.getAllFavourites(request)
        return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})
    else:
        return redirect('home')



# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = services.getAllFavourites(request)
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    services.saveFavourite(request)
    return redirect('home')

@login_required
def deleteFavourite(request):
    services.deleteFavourite(request)
    return redirect('favoritos')

@login_required
def exit(request):
    logout(request)
    return redirect('login')