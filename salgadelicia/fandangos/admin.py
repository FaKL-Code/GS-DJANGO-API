from django.contrib import admin
from fandangos.models import Doacao, Doador

class Doadores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'telefone', 'endereco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

class Doacoes(admin.ModelAdmin):
    list_display = ('id', 'doador', 'volume', 'data_doacao', 'data_retirada')
    list_display_links = ('id', 'doador')
    search_fields = ('doador',)
    list_per_page = 20
    
admin.site.register(Doador, Doadores)
admin.site.register(Doacao, Doacoes)