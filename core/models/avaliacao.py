from django.db import models
from .livro import Livro
from .editora import Editora
from .categoria import Categoria

class Avaliacao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, editable=False) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, editable=False)  
    comentario = models.TextField()
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.livro:
            self.editora = self.livro.editora
            self.categoria = self.livro.categoria
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Avaliação de {self.livro.titulo} ({self.nota}/5)'