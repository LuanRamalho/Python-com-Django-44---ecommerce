from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('adicionar-ao-carrinho/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('ver-carrinho/', views.ver_carrinho, name='ver_carrinho'),
]
