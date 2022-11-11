from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'galerias/galerias.html')

def ceu_will(request):
    return render(request, 'galerias/ceu_will.html')

def cole_will(request):
    return render(request, 'galerias/colecao_will.html')

def festa_kelly(request):
    return render(request, 'galerias/festa_kelly.html')

