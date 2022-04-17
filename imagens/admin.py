from django.contrib import admin
from imagens.models import Imagem


class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao')


admin.site.register(Imagem, ImagemAdmin)
