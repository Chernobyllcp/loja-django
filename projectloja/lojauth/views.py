from django.shortcuts import render

def cadastrar(request):
    return render(request,'auth/cadastrar.html' )
