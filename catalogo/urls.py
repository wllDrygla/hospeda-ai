from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('modelo01/', views.modelo01, name='modelo01')

]