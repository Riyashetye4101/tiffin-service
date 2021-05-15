from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.models import ServiceProvider
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('user')

@csrf_exempt
def userlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None and user.is_customer == True:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    return render(request,'app/user.html')
    
@csrf_exempt
def adminlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None and user.is_sp == True:
            login(request,user)
            return redirect('order')
        else:
            messages.info(request,'Username or Password is incorrect')

    return render(request,'app/admin1.html')

