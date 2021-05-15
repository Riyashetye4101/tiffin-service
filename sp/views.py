from django.shortcuts import render, redirect, get_object_or_404
from account.models import *
from sp.forms import MenuForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from datetime import datetime
from django.db.models import Q
# Create your views here.



def adminentry(request):
    sp = get_object_or_404(ServiceProvider,user=request.user)
    cust = sp.customer.all()
    return render(request,'sp/adminaccount.html',{'cust':cust})


@csrf_exempt
def menu(request):
    # tsp = User.objects.get(id=request.user.id)
    admin = get_object_or_404(ServiceProvider, pk=request.user.id)
    menu = Menu.objects.filter(sp=admin).order_by('-id')

    if request.method == 'POST':
        item_name = request.POST.get('item')
        price = request.POST.get('price')
        cat = request.POST.get('category')
        add_menu = Menu(sp=admin,item_name=item_name,price=price,category=cat)
        if item_name=='' or price=='' or cat=='':
            messages.info(request,'please fill all the empty space')
        else:
            add_menu.save()
            
        return redirect('menu')

    context={'menu':menu}
    return render(request,'sp/menuupdate.html',context)


def delete(request,pk_test):
    item = get_object_or_404(Menu,id=pk_test)
    item.delete()
    return redirect('menu')

    


def order(request):
    tsp = get_object_or_404(ServiceProvider,user=request.user)
    context=dict()
    try:
        order=Order.objects.filter(sp=tsp,last_date__gte=datetime.now())
        context['order']=order
        context['total']=order.count()
        check = True
    except:
        check = False
    context['check']=check
    return render(request,'sp/order.html',context)


def customerdetails(request,cust_id):
    cust = get_object_or_404(Customer,user=cust_id)
    tsp = get_object_or_404(ServiceProvider,user=request.user)
    cust_order = Order.objects.filter(customer=cust,sp=tsp).order_by('-date_of_order') 
    total = cust_order.count()
    context={'order':cust_order,'cust':cust,'total':total}
    return render(request,'sp/cd.html',context)

def status(request,order_id):
    order = get_object_or_404(Order,id=order_id)
    menu = CustomerMenuItem.objects.filter(order=order)
    address = Address.objects.filter(placeanorder=order).order_by('-date_create')
    context = {'order':order,'menu':menu,'add':address[0]}
    return render(request,'sp/status.html',context)

def details(request,cd_id):
    o = get_object_or_404(Order,id=cd_id)
    menu = CustomerMenuItem.objects.filter(order=o)
    add = Address.objects.filter(placeanorder=o).order_by('-date_create')[0]
    return render(request,'sp/past_order.html',{'order':o,'menu':menu,'add':add})
   



