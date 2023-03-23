from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages





def cadastrar(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirme_password = request.POST['pass2']
        if password != confirme_password:
            messages.warning(request,"SENHA E CONFIRMAÇÃO NÃO CORRESPONDEM!")
            return render(request,'auth/cadastrar.html')
        
        
        try:
            if User.objects.get(usarname=email):
                messages.warning(request,"Este email já é cadastrado")
                return render(request,'auth/cadastrar.html')
        except Exception as identifier:
            pass
        
        myuser = User.objects.create_superuser(email, email, password)
        myuser.save()
        messages.info(request,"Cadastro realizado com sucesso. Faça seu login!!")
        return redirect('/lojauth/login')
    return render(request,'auth/cadastrar.html' )



def handlelogin(request):
    return render(request,'auth/login.html' )
