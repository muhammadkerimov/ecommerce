"""
URL configuration for socialkingaz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views             

urlpatterns = [
    path('orders',views.orders,name='indexadmin'),
    path('login',views.login,name='loginadmin'),
    path('reg',views.register,name='reg'),
    path('customers',views.customers,name='customerspage'),
    path('orders/<str:orderid>',views.orderview,name='adminorder'),
    path('logout',views.logout,name='logoutadmin'),
    path('products',views.products,name='productsadmin'),
    path('products/add-product',views.addproduct,name='addproduct'),
    path('products/<str:prodid>',views.productInfo,name='prodview'),
    path('testingserver',views.testingserver,name='test'),
    
]
