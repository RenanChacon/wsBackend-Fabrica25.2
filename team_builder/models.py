from django.db import models

class Time(models.Model):
    nome_time = models.CharField(max_length=100)
    nome_jogo = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome_time} ({self.nome_jogo})"

class Pokemon(models.Model):
    nome = models.CharField(max_length=20)
    apelido = models.CharField(max_length=50, blank=True)
    nivel = models.IntegerField()
    tipo = models.CharField(max_length=20)
    imagem = models.URLField()
    time = models.ForeignKey(Time, related_name='pokemons', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nome} / Time: {self.time.nome_time}"