from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Detial
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("lname", "")
        password = request.POST.get("lpass", "")
        if not username and not password:
            messages.info(request,"Empty credentials")
            return redirect('/')
        user = auth.authenticate(username = username,password = password)
        if user:
            auth.login(request,user)
            return redirect("/chat/")

        else:
            messages.info(request,"Invalid detials")
            return redirect("/")
    return render(request,'login.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("uname","")
        password = request.POST.get("upass","")

        if not username and not password:
            messages.info(request,"Empty credentials")
            return redirect('/signin/')
        get_data = User.objects.filter(username = username,password = password)
        if get_data:
            messages.info(request,"User already exists")
            return redirect('/signin/')

        create = User.objects.create_user(username = username,password = password,email = "a@gmail.com")
        create.save()
        return redirect("/")


    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def chat(request):
    get_data = Detial.objects.all()
    context = {
        'get_data' : get_data
    }
    return render(request,'chat.html',context)