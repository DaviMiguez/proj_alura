from django.shortcuts import render

def index(request):
    receitas = {
        1:'Arroz',
        2:'Feijão',
        3:'Farofa',
        4:'Strogonoff',
        5:'Lasanha',
        6:'Bolo de fubá'
    }

    dados = {
        'nome_das_receitas' : receitas
    }
    
    return render(request,'index.html', dados)

def receita(request):
    return render(request, 'receita.html')