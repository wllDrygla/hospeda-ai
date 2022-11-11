from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'catalogo/catalogo.html')

def modelo01(request):
    return render(request, 'catalogo/modelo01.html')