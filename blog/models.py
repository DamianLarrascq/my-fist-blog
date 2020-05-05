from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        blank=True, null=True)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Articulo(models.Model):
    nombreArticulo = models.CharField(max_length=200)
    caracteristica = models.CharField(max_length=200)
    clasificacion = models.CharField(max_length=200)
    temporadas = models.ForeignKey('Temporadas', on_delete=models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreArticulo

    def guardar(self):
        self.save()


class Tela(models.Model):
    nombreTela = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    proovedor = models.ForeignKey('proov_telas', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.nombreTela

    def guardar(self):
        self.save()


class ArticuloUsaTela(models.Model): # CLASE DE ASOCIACION ENTRE ARTICULO Y TELA PARA AGREGARLE UN USO A UNA TELA
    articuloID = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING, blank=True, null=True)
    uso = models.CharField(max_length=100)
    tela = models.ForeignKey(Tela, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.tela.nombreTela

    def guardar(self):
        self.save()


class proov_telas(models.Model):
    nombreProov = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)


class Temporadas(models.Model):
    nombreTemporada = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFinal = models.DateField()
    anio = models.CharField(max_length=4)


    def __str__(self):
        return self.nombreTemporada + ' ' + self.anio

class ArtEnTemporada(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING, blank=True, null=True)
    temporada = models.ForeignKey(Temporadas, on_delete=models.DO_NOTHING, blank=True, null=True)