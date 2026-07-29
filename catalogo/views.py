from django.shortcuts import render

def catalogo_produtos(request):
    produtos = [
        {"nome": "Notebook", "preco": 3500.00},
        {"nome": "Mouse", "preco": 79.90},
        {"nome": "Teclado Mecânico", "preco": 250.00},
        {"nome": "Monitor 24''", "preco": 899.00},
    ]
    return render(request, 'catalogo/catalogo.html', {"produtos": produtos})