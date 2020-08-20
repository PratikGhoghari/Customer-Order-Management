from django.urls import path
from . import views

urlpatterns=[
    path('customers/',views.getCustomers,name='customers'),
    path('customer_orders/<int:pk>/',views.getCustomerProducts,name='customer_orders'),
    path('create_customer/',views.createCustomer,name='create_customer'),
    path('products/',views.getProducts,name='api_products'),
    path('',views.apiOverview,name='api_overview'),
    path('create_order/<int:pk>',views.createOrder,name='create_order')
]