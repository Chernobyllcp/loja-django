import email
from email.message import EmailMessage
from email.mime import message
from lib2to3.pgen2 import token
from logging import exception
from tokenize import generate_tokens
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from .utils import TokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import NoReverseMatch, reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.mail import BadHeaderError, send_mail
from django.core import mail 
from django.conf import settings




def cadastrar(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirme_password = request.POST['pass2']
        if password != confirme_password:
            messages.warning(request,"SENHA E CONFIRMAÇÃO NÃO CORRESPONDEM!")
            return render(request,'auth/cadastrar.html')
        
        
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Este email já é cadastrado")
                return render(request,'auth/cadastrar.html')
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email, email, password)
        user.is_active=False
        user.save()
        current_site = get_current_site(request)
        email_subject = "Ative sua conta"
        messages=render_to_string('lojauth/activate.html',{  
            'user':user,
            'domain':127.0.0.1:8000,
            'uid':urlsafe_base64_decode(force_bytes(user.pk)),
            'token':generate_tokens.make_token(user)   
        })
        email_massage = EmailMessage(email_subject,message.settings.EMAIL_HOST_USER,[user])
        EmailThread(email_massage).start()
        
        messages.info(request,"Foi enviado um link no seu e-mail para você ativar sua conta.")
        return redirect('/lojauth/login')
    return render(request,"auth/cadastrar.html")



def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username,password=userpassword)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request,"Login com sucesso !")
            return render(request,'index.html')
        
        else:
            messages.error(request,"Senha ou e-mail não corresponde")
            return redirect('/lojauth/login')
    return render(request,'auth/login.html' )


def handlelogout(request):
    logout(request)
    messages.success(request,"Saida do sistema com sucesso.")
    return redirect('/lojauth/login')

