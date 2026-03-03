from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # Página inicial
    path('cadastrar/', views.criar_produto, name='criar_produto'),  # Formulário
    path('lista/', views.lista_produtos, name='lista_produtos'),    # Lista de produtos
]