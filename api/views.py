from django.shortcuts import render
from rest_framework.response import Response
from accounts.models import Customer,Order, Product
from .serializers import *
from rest_framework.decorators import api_view

# Not necessary to check for GET and POST request since decorators handles that.

@api_view(['GET'])                                  # This function only gets called for GET request.
def getCustomers(request):
    if request.method == 'GET':
        customers  = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
        return Response(customer_serializer.data)


@api_view(['GET'])
def  getCustomerProducts(request,pk):
    if request.method == 'GET':
        customer = Customer.objects.get(id=pk)           
        customer_products = Order.objects.filter(customer=customer)       # Get all the orders for a particular customer.
        customer_products_serializer = CustomerOrderSerializer(customer_products, many=True)
        return Response(customer_products_serializer.data)


@api_view(['POST'])
def createCustomer(request):
    if request.method=='POST':                                
        customer = CustomerSerializer(data=request.data)
        if customer.is_valid():
            customer.save()
        return Response(customer.data)


@api_view(['GET'])
def getProducts(request):
    if request.method == 'GET':   
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)
   

@api_view(['GET'])
def apiOverview(request):
    context={
        'customers/':'Retrieve Customers',
        'customer_orders/<customer id>/':'Get the orders for a particular customer',
        'create_customer/':'Create a new Customer',
        'products/':'Retrieve all the products'
    }
    return Response(context)


@api_view(['POST'])
def createOrder(request,pk):
    #customer = Customer.objects.get(id=pk)
    order = OrderSerializer(request.POST)
    if order.is_valid():
        order.save()
    return Response(order.data)