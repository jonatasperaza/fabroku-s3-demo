from django.contrib import admin
from django.utils.html import format_html

from .models import Foto


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['miniatura', 'titulo', 'arquivo', 'enviada_em']
    readonly_fields = ['previa', 'arquivo']
    fields = ['titulo', 'imagem', 'previa', 'arquivo']

    @admin.display(description='')
    def miniatura(self, obj):
        return format_html('<img src="{}" style="height:48px;border-radius:6px">', obj.imagem.url) if obj.imagem else ''

    @admin.display(description='Prévia')
    def previa(self, obj):
        return format_html('<img src="{}" style="max-height:240px;border-radius:8px">', obj.imagem.url) if obj.imagem else '-'

    @admin.display(description='Caminho no bucket')
    def arquivo(self, obj):
        return obj.imagem.name
