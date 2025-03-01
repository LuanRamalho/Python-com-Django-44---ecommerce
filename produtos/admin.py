from django.contrib import admin
from .models import Produto, Categoria

# Registrar o modelo Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Campos que serão exibidos na lista
    search_fields = ('nome',)  # Adiciona uma barra de pesquisa para o nome da categoria

# Registrar o modelo Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'data_adicao')  # Campos que serão exibidos na lista
    list_filter = ('categoria',)  # Filtro para listar produtos por categoria
    search_fields = ('nome', 'descricao')  # Adiciona pesquisa por nome e descrição
    list_per_page = 10  # Define o número de produtos por página na listagem
    ordering = ('-data_adicao',)  # Ordena os produtos pela data de adição, do mais recente para o mais antigo

# Registrar os modelos com o Django Admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
