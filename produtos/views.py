from django.shortcuts import render, redirect
from .models import Produto, Categoria
from .forms import ProdutoForm

# View para cadastro de produtos (Somente para admin)
def cadastrar_produto(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = ProdutoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('listar_produtos')
        else:
            form = ProdutoForm()
        return render(request, 'produtos/cadastrar_produto.html', {'form': form})
    else:
        return redirect('listar_produtos')

# Função que processa o carrinho
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        produtos_selecionados_ids = request.POST.getlist('produtos_selecionados')
        produtos_selecionados = Produto.objects.filter(id__in=produtos_selecionados_ids)
        
        # Armazenando os produtos selecionados no carrinho (em um session, por exemplo)
        request.session['carrinho'] = [produto.id for produto in produtos_selecionados]
        
        # Redirecionar para a página de visualização do carrinho
        return redirect('ver_carrinho')

# Página do carrinho de compras
def ver_carrinho(request):
    carrinho = request.session.get('carrinho', [])
    produtos_no_carrinho = Produto.objects.filter(id__in=carrinho)
    
    # Calcular o total
    total = sum(produto.preco for produto in produtos_no_carrinho)
    
    return render(request, 'produtos/ver_carrinho.html', {
        'produtos': produtos_no_carrinho,
        'total': total
    })
