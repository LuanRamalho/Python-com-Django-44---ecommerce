from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    imagem = models.URLField(max_length=500)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
