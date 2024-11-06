# financeiro/admin.py

from django.contrib import admin
from .models import (
    Receita, FonteReceita, Despesa, CategoriaDespesa, 
    FolhaPagamento, Cargo, Licitacao, StatusLicitacao, 
    Contrato, StatusContrato, PrestacaoContas
)

admin.site.register(Receita)
admin.site.register(FonteReceita)
admin.site.register(Despesa)
admin.site.register(CategoriaDespesa)
admin.site.register(FolhaPagamento)
admin.site.register(Cargo)
admin.site.register(Licitacao)
admin.site.register(StatusLicitacao)
admin.site.register(Contrato)
admin.site.register(StatusContrato)
admin.site.register(PrestacaoContas)
