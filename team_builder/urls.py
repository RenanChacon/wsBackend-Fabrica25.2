from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('times/', views.lista_times, name='lista_times'),
    path('times/criar/', views.criar_time, name='criar_time'),
    path('times/<int:time_id>/', views.detalhe_time, name='detalhe_time'),
    path('times/<int:time_id>/editar/', views.editar_time, name='editar_time'),
    path('times/<int:time_id>/excluir/', views.excluir_time, name='excluir_time'),
    path('times/<int:time_id>/adicionar_pokemon/', views.adicionar_pokemon, name='adicionar_pokemon'),
    path('pokemon/<int:pokemon_id>/', views.detalhe_pokemon, name='detalhe_pokemon'),
    path('pokemon/<int:pokemon_id>/excluir/', views.excluir_pokemon, name='excluir_pokemon'),
]
