from django.contrib import admin
from.models import Medicamento, Cliente

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'preco', 'estoque'

class ClienteAdmin(admin.ModelAdmin):
    list_display = 'nome', 'sobrenome', 'email'

admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Cliente, ClienteAdmin)
# Register your models here.
