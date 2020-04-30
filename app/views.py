from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Produto


def home(request):
    return render(request, 'home.html')

def produto(request):
    return render(request, 'produto.html')


def list_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    try:
        data['list'] = Produto.objects.all()
    except:
         data['error'].append("Erro ao carregar produto! ")
    return render(request, 'listarproduto.html', data)


@csrf_exempt
def new_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []

    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        cod = request.POST.get('cod')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        qtd = request.POST.get('qtd')
        try:
            if (id == -1):
                data['error'].append("Produto Cadastrado!!! ")
                produto = Produto(cod=cod, nome=nome, preco=preco, qtd=qtd)
                produto.save()

            else:
                data['error'].append("Produto Alterado!!! ")
                produto = Produto.objects.get(id=id)
                produto.cod = cod
                produto.nome = nome
                produto.preco = preco
                produto.qtd = qtd
                produto.save()


        except:
            data['error'].append("Erro ao cadastrar produto!!! ")
            return render(request, 'produto.html', data)

        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produto!!! ")
            return render(request, 'produto.html', data)
        return render(request, 'produto.html', data)
    else:

        return render(request, 'produto.html', data)


def delete_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            produto= Produto.objects.get(id=id)
            produto.delete()
        except:
            data['error'].append("Erro ao deletar produto!!! ")
            return render(request, 'listarproduto.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produto!!! ")
            return render(request, 'produto.html', data)
        return render(request, 'listarproduto.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'listarproduto.html', data)


def update_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['produto'] = []
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            data['produto'].append(Produto.objects.get(id=id))
        except:
            data['error'].append("Erro ao carregar produto!!! ")
            return render(request, 'clients.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produto!!! ")
            return render(request, 'produto.html', data)
        return render(request, 'produto.html', data)
    else:
        data['Error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'produto.html', data)
