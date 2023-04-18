from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, related_name='atracoes')
    comentarios = models.ManyToManyField(Comentario, related_name='comentarios')
    avaliacoes = models.ManyToManyField(Avaliacao, related_name='avaliacoes')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    @property
    def descricao_completa2(self):
        return f'{self.nome} - {self.descricao}'

    def __str__(self):
        return self.nome






