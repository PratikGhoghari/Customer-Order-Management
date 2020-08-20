from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
# Create your views here.

def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()    

    context={
        'customers':customers,
        'orders':orders,
        'total_orders':total_orders,
        'total_customers':total_customers,
        'delivered':delivered,
        'pending':pending
    }
    return render(request,'accounts/dashboard.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'accounts/register.html',context)

def loginPage(request):
    
    context={}
    return render(request,'accounts/login.html',context)

def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def customers(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()   # Get all the orders for a particular customer
    orders_count=orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders) # request.GET is the data we are filtering for onqueryset which is all the orders of specific customer.
    orders=myFilter.qs
    context={
        'customer':customer,
        'orders':orders,
        'orders_count':orders_count,
        'myFilter':myFilter
    }    
    return render(request,'accounts/customers.html',context)

def createCustomer(request):
    customer_form = CustomerForm()
    if request.method=='POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/')
    context={
        'customer_form':customer_form
    }
    return render(request,'accounts/create_customer.html',context)

def createOrder(request):
    form = OrderForm()
    if request.method=='POST':
        form = OrderForm(request.POST) # form data is passed from request object
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)

    context={
        'form':form
    }
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order) # Updating the existing order where request.post has the updated data and passed to OrderForm
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    context={
        'order':order
    }
    if request.method=="POST":
        order.delete()
        return redirect('/')
    return render(request,'accounts/delete_order.html',context)

