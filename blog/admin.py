from django.contrib import admin
from .models import Post
from .models import Tela, Articulo, ArticuloUsaTela, Temporadas


admin.site.register(Post)
# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombreArticulo', 'caracteristica', 'clasificacion', 'temporadas')

admin.site.register(Articulo, ArticuloAdmin)

class TelaAdmin(admin.ModelAdmin):
    list_display = ('nombreTela', 'color')

admin.site.register(Tela, TelaAdmin)

class ArticuloUsaTelaAdmin(admin.ModelAdmin):
    list_display = ('articuloID', 'uso', 'tela')
