from django.http import HttpResponse  # Necesario para poder responder al cliente
from django.shortcuts import render  # Necesario para que funcione la otra forma de visualizar una vista

# Con HttpResponse, podemos responder con texto plano o con HTML
# Forma de responder al cliente cuando hace una solicitud HTTP
def index(request):  # El request captura las peticiones de los clientes
    return HttpResponse("<h1>Hola mundo</h1>")

# Con esto hemos habilitado una vista, pero hay que darla de alta en urls.py
def home(request):  # Pinta una página con render, también hay que darla de alta en urls.py
    return render(request, 'index.html')  # La página index.html debe crearse

# Vista para la página secundaria del proyecto
def pagina2(request):
    return render(request, 'pagina2.html')