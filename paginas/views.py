from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'paginas/pagina.html')

def psikelly(request):
    return render(request, 'paginas/psikelly.html')

def tiochico(request):
    return render(request, 'paginas/tiochico.html')

