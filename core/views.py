from django.shortcuts import render, get_object_or_404
from .models import Medicamento


def index(request):
    medicamentos = Medicamento.objects.all()

    conteudos = {
        'curso': 'programação - Django Framework',
        'medicamentos': medicamentos
    }

    return render(request, 'index.html', conteudos)


def contato(request):
    return render(request, 'contato.html')


def detalhe(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)

    return render(
        request,
        'detalhe.html',
        {'medicamento': medicamento}
    )