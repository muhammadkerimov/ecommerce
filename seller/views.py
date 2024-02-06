from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages as mesajlar
from .models import adminaccs
from datetime import datetime
from django.core.mail import EmailMessage , send_mail
from users.models import order , customer , product
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import vonage
# Create your views here.
import random , string 
import http.client
import json
def ran_gen(size, chars=string.ascii_uppercase + string.digits):

  return ''.join(random.choice(chars) for x in range(size))

client = vonage.Client(key="150f9ed9", secret="d7vYqowCrgm1GbH6")
def islogin(request):
    if request.session.get('adminName'):
        return True
    else:
        return False
    
def orders(request):
  if islogin(request):
    orders = order.objects.all().values()
    context = {
       'orders':orders
    }
    return render(request,'ordersadmin.html',context)
  else:
     return redirect('loginadmin')
  
def login(request):
   if islogin(request)==False:
    if request.method == 'POST':
       admin_ID = request.POST['adminID']
       admin_Password = request.POST['adminPassword']
       userFind = adminaccs.objects.all().filter(admin_id=admin_ID,admin_password=admin_Password).values()
       if len(userFind)>0:
          userTime = adminaccs.objects.all().get(admin_id=admin_ID)
          userTime.admin_login_last = datetime.now()
         
          request.session['adminName'] = userFind[0]['admin_name']
          request.session['adminID'] = userFind[0]['admin_id']
          userTime.save()
          return redirect('indexadmin')
       else:
         mesajlar.error(request,'User Not Found!')
         return redirect('loginadmin')
    return render(request,'adminlogin.html')
   else:
      return redirect('indexadmin')
   
def register(request):
   newUser = adminaccs(
      admin_name='Muhammad',
      admin_surname = 'Karimov',
      admin_id = '291192',
      admin_password = 'test',
      admin_level = 'level5',
      admin_login_last = datetime.now()
   )
   newUser.save()
   return HttpResponse('Success')

def orderview(request,orderid):
  if islogin(request):
   if request.method == "POST":
      deliveryOrder = order.objects.all().get(order_id=orderid)
      deliveryOrder.admin_delivery_status = 1
      deliveryOrder.admin_delivery = request.POST['adminDeliver']
      userMail = customer.objects.all().get(user_id=deliveryOrder.user_id)
      userMail = userMail.email
      mailCont = {
         'orderidmail':orderid,
         'order_link':f'http://127.0.0.1:8000/order/{orderid}'
      }
      messagemail = render_to_string('mailtemp.htm',mailCont)
   
      mail =EmailMessage(
            subject=f'Your Order With ID {deliveryOrder.order_id} Completed!',
            body=messagemail,
          from_email='socialking@englishexamhub.xyz' ,
          to= [request.POST['userMAIL'],]
        )


     
      mail.content_subtype = 'html'
      mail.send()
      deliveryOrder.save()
      return redirect('indexadmin')
   userOrder = order.objects.all().filter(order_id=orderid).values()
   orderProds = userOrder[0]['product_id_and_quantities']
   userMail = customer.objects.all().filter(user_id=userOrder[0]['user_id']).values()[0]['email']
   context = {
      'orderProds':orderProds,
      'order_total':userOrder[0]['order_total_payment'],
      'order_son':userOrder[0]['payment_son'],
      'orderID':userOrder[0]['order_id'],
      'userEmail':userMail,
      'userNotes':userOrder[0]['additional_notes'],
      'adminDelivery':userOrder[0]['admin_delivery'],
      'adminDS':userOrder[0]['admin_delivery_status'],
      'paymentDate':userOrder[0]['payment_date'] 
   }
   return render(request,'orderview.html',context)
  else:
      return redirect('loginadmin')
  
def customers(request):
 if islogin(request):
   customersData = customer.objects.all().values()
   return render(request,'customerspage.html',{'customers':customersData})
 else:
    return redirect('loginadmin')

def products(request):
   if request.method == "POST":
      deleteProd = product.objects.all().get(product_id=request.POST['deleteProd'])
      deleteProd.delete()
      mesajlar.success(request,'Succesfully Deleted!')
      return redirect(request.path_info)
   allProds = product.objects.all().values()
   contextProd = {
      'products':allProds
   }
   return render(request,'prodadmin.html',contextProd)

def productInfo(request,prodid):
 if islogin(request):
   if request.method == "POST":
      productChange = product.objects.all().get(product_id=prodid)
      if len(request.FILES)>0:
       productChange.product_image = request.FILES['prodFile']
      productChange.name = request.POST['prodName']
      productChange.price = request.POST['prodPrice']
      productChange.info = request.POST['prodInfo']
      productChange.discount = request.POST['prodDisc']
      productChange.save()
      mesajlar.success(request,'Succesfully Changed!')
      return redirect(request.path_info)
   productFilter = product.objects.all().get(product_id=prodid)
   productFilter.price = str(productFilter.price).replace(',','.')
   productFilter.discount = str(productFilter.discount).replace(',','.')
   contextProd = {
      'product':productFilter
   }
   return render(request,'prodview.html',contextProd) 
 else:
    return redirect('loginadmin')


def addproduct(request):
   if request.method == 'POST':
      newProd = product(
         name = request.POST['prodName'],
         info = request.POST['prodInfo'],
         price = request.POST['prodPrice'],
         product_id = ran_gen(10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'),
         product_image = request.FILES['prodFile'],
         discount = request.POST['prodDiscount'],
         comment_ids = [0],
         review_ids = [0]
      )
      newProd.save()
      return redirect('productsadmin')
   return render(request,'addprod.html')


def testingserver(request):
   return HttpResponse(request.META['HTTP_HOST'])

def logout(request):
   request.session.flush()
   return redirect('loginadmin')

