from django.shortcuts import render, get_object_or_404, redirect
from account.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import timedelta
from datetime import datetime
from datetime import date
from django.db.models import Q


# Create your views her

@csrf_exempt
def home(request):
    companies = ServiceProvider.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if search is not None:
            companies = ServiceProvider.objects.filter(Q(city__contains=search) | Q(state__contains=search))
        
    context = {'companies':companies}
    return render(request,'customer/home.html',context)



def detail(request,id_test):
    login=False
    user1= get_object_or_404(User,pk=id_test)
    tsp = get_object_or_404(ServiceProvider,user=user1)
    customer=get_object_or_404(Customer,user=request.user)
    under=customer.serviceprovider_set.all()
    for admin in under:
        if admin==tsp:
            login=True
    return render(request,'customer/details.html',{'tsp':tsp,'login':login})




def add_sp(request, pk_test):
    user1= get_object_or_404(User,pk=pk_test)
    tsp = get_object_or_404(ServiceProvider,user=user1)
    customer=get_object_or_404(Customer,user=request.user)
    tsp.customer.add(customer)
    return redirect('home')

def account(request):
    customer=get_object_or_404(Customer,user=request.user)
    tsp=customer.serviceprovider_set.all()
    return render(request,'customer/account.html',{'tsp':tsp})

@csrf_exempt
def update_menu(request,id_order):
    order = get_object_or_404(Order,id=id_order)
    use = get_object_or_404(User,id=order.sp.user.id)
    tsp = get_object_or_404(ServiceProvider,user=use)
    menu = Menu.objects.filter(sp=tsp)
    context = {'menu':menu,'order':order}
    try:
        order_menu = CustomerMenuItem.objects.filter(order=order)
        check = True
    except:
        check = False
    if check:
        amount = 0.0
        for i in order_menu:
            amount+=float(i.price)
        context['ordered_menu']=order_menu
        context['total']=amount
        order.total_amount = amount
        order.save()
    return render(request,'customer/visite.html',context)

def add_item(request,item_id,order_id):
    order = get_object_or_404(Order,id=order_id)
    if request.method == 'POST':
        item = Menu.objects.get(id=item_id)
        price = float(request.POST.get('Quantity'))*float(item.price)
        quantity = request.POST.get('Quantity')
        add_menu = CustomerMenuItem(
            order = order, item_name=item.item_name, price=price, quantity=quantity
            )
        add_menu.save()
    return redirect(update_menu,id_order=order_id)

def remove(request,id1):
    user1= get_object_or_404(User,pk=id1)
    tsp = get_object_or_404(ServiceProvider,user=user1)
    cust=get_object_or_404(Customer,user=request.user)
    tsp.customer.remove(cust)
    return redirect('your_account')


def delete(request,reset_id,pl):
    order = get_object_or_404(Order,pk=pl)
    item = get_object_or_404(CustomerMenuItem,id=reset_id)
    item.delete()
    return redirect(update_menu,id_order=order.pk)


def order(request):
    user = get_object_or_404(User,id=request.user.id)
    customer = get_object_or_404(Customer,user=user)
    context = dict()
    try:
        order = Order.objects.filter(customer=customer)
        context = {'orderlist':order}
        check = True
    except:
        check = False
    context['check']=check
    return render(request,'customer/order.html',context)



def cancel(request,order_id):
    order = get_object_or_404(Order,id=order_id)
    order.delete()
    return redirect('user_order')

def order_address(request,or_id):
    order = get_object_or_404(Order,id=or_id)
    context = {'order':or_id}
    try:
        address = Address.objects.filter(placeanorder=order).order_by('-id')
        context['address']=address
    except:
        print('no data present still')
    if request.method == 'POST':
        state = request.POST.get('state')
        city = request.POST.get('city')
        pinno = request.POST.get('pinno')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        Building = request.POST.get('Building')
        houseno = request.POST.get('houseno')
        add = Address(
            placeanorder=order,
            state= state,city=city,pin_no=pinno,Area_name=area,land_mark=landmark,
            building_name=Building,flate_number=houseno
            )
        add.save()
        return redirect('address',or_id=or_id)

    return render(request,'customer/update_add.html',context)

def select(request,sp_id):
    sp = get_object_or_404(ServiceProvider,user=sp_id)
    cust = get_object_or_404(Customer,user=request.user)
    context = {'company':sp}
    try:
        orders = Order.objects.filter(sp=sp,customer=cust).order_by('-id')
        create_order = orders[0]
        check = True
    except :
        check = False
    if check:
        context['order']=create_order
        today = date.today()
        lastdate = create_order.last_date.date()
        if today > lastdate:
            check = False
    context['check']=check
    
    return render(request,'customer/select.html',context)

def duration(request,data,company_id):
    if data == '7':
        dur = 'For one week'
    elif data == '31':
        dur = 'For one month'
    elif data == '183':
        dur = 'For six month'
    else :
        dur = 'For one year'
    cust = get_object_or_404(Customer,user=request.user)
    sp = get_object_or_404(User,id=company_id)
    company = get_object_or_404(ServiceProvider,user=sp)
    order = Order(
        sp = company, customer = cust, duration= dur, no_of_orders=data,
        )
    order.save()
    lastdate = order.date_of_order + timedelta(days=int(order.no_of_orders))
    order.last_date = lastdate
    order.save()
    return redirect(select,sp_id=sp.id)
    
def tiffin(request,pk_order):
    order = get_object_or_404(Order,id=pk_order)
    address = Address.objects.filter(placeanorder=order).order_by('-date_create')
    menu = CustomerMenuItem.objects.filter(order=order)
    context = {'order':order,'address':address[0],'menu':menu}
    return render(request,'customer/tiffin.html',context)
