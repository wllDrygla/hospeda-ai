from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cv/cvmodelo.html')

def will(request):
    return render(request, 'cv/will.html')