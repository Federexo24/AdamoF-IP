# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
import requests
from ..transport import transport
from ..utilities import translator

def getAllImages():
    # Obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = transport.getAllImages() # Llama a la API y obtiene datos en crudo
    images = []  # Lista para almacenar los objetos Card

    # Recorre cada dato crudo de la colección y lo convierte en una Card
    for obj in json_collection:
        card = translator.fromRequestIntoCard(obj)  # Transforma el objeto JSON crudo en un objeto Card
        images.append(card)  # Agrega la Card a la lista de imágenes

    return images  # Retorna la lista de Cards listas para ser usadas en el template

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.