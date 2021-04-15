from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    conteudo = models.CharField(
        max_length=200, null=False, blank=False, unique=False, verbose_name="Postagem")
    data_criacao = models.DateTimeField(editable=False)
    data_edicao = models.DateTimeField()
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=True)

    def save(self, *args, **kwargs):
        # Atualizar datas criacao edicao
        if not self.data_criacao:
            self.data_criacao = timezone.now()
        self.data_edicao = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    @property
    def formt_criacao(self):
        return 'Criado na data de {}/{}/{} ás {} horas,'.format(self.data_criacao.day, self.data_criacao.month,
                                                                self.data_criacao.year, self.data_criacao.time())

    def __str__(self):
        return self.conteudo
