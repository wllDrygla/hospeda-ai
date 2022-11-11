from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('ceu_will/', views.ceu_will),
    path('colecao_will/', views.cole_will, name='cole_will'),
    path('festa_kelly/', views.festa_kelly, name='festa_kelly'),

]