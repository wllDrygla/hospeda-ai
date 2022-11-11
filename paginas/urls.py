from django.urls import path
from . import views
urlpatterns = [
    #inicio
    path('', views.index, name='index'),

    #pagina kelly
    path('psikelly', views.psikelly, name='psikelly'),

    #pagina TioChico
    path('chico-carpinteiro', views.tiochico, name='tiochico'),


]