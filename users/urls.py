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
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('register',views.signup,name='signup'),
    path('product/<str:id>',views.productsee,name='product'),
    path('cart',views.cart,name='shoppingcart'),
    path('logout',views.logout,name='logout'),
    path('profile',views.userprofile,name='profile'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.userorders,name='orders'),
    path('proccesing',views.check_payment,name='check'),
    path('success',views.successpay,name='success'),
    path('failure',views.failure,name='failure'),
    path('order/<str:id>',views.getorderdat,name='orderdetails'),
    path('addbalance',views.addbalance,name='addbalance'),
    path('error',views.errorReq,name='error404')
]
