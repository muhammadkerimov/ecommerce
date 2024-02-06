from django.shortcuts import render , redirect
from .models import customer , product , shoppingcart , review , categories , order
from django.contrib import messages
from django.conf import settings
import random
import json , string
import time
import stripe
from django.http import HttpResponse
from django.core.mail import send_mail
from datetime import datetime
import string

stripe.api_key = 'sk_test_51M1aAoJilhQEZGyd2yLJw9XO6RdljJyJTLy3gz2alTBpaGsP4nOvUc4zqwfUUa8gvlnBpynDKxVAYab6cuAmxesp00lIXCx44G'
def ran_gen(size, chars=string.ascii_uppercase + string.digits):

  return ''.join(random.choice(chars) for x in range(size))



def ran_gen1(size, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for x in range(size))

 

# function call for random string

# generation with size 8 and string
# 


def errorReq(request):
   return render(request,'404.html')
def index(request):

    items = product.objects.all().values()
    procategories = categories.objects.all().values()
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    context = {
        'items':items,
        'categories':procategories,
        'basket':bas
    }
    return render(request,'index.html',context)

def shop(request):
    products = product.objects.all().values()
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    context = {
        'products':products,
        'basket':bas
    }
    return render(request,'shop-grid.html',context)

def contact(request):
    if request.method == "POST":
        userName = request.POST['userName']
        userMail = request.POST['userEmail']
        userMessage = request.POST['textMessage']
        a = send_mail(
            subject=f'Message From {userName}',
            message=f'''Name : {userName} 
Email : {userMail}
Message : {userMessage}
             ''',
          from_email=userMail ,
          recipient_list= ['socialking@englishexamhub.xyz',]
        )
        messages.success(request,'Successfully Sent!')
        return redirect('contact')
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    context = {
        'basket':bas
    }
    return render(request,'contact.html',context)

def login(request):
    if request.method == "POST":
        userMail = request.POST['customerEmail']
        userPassword = request.POST['customerPass']
        checkUser = customer.objects.all().filter(
            email = userMail,
            password = userPassword
        ).values()
        if len(checkUser)>0:
            request.session['userID']= checkUser[0]['user_id']
            request.session['userName'] = checkUser[0]['name']
            request.session['orderedProd'] = checkUser[0]['ordered_products']
            request.session['userBalance'] = checkUser[0]['balance']
            return redirect('index')
        else:
           messages.error(request,'Entered Details Is Not Valid!')
           return redirect('login')
    
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('index')

def signup(request):
    if request.method == "POST":
        userName = request.POST['name']
        userSurname = request.POST['surname']
        userFatherName = request.POST['fathername']
        userEmail = request.POST['email']
        userPhoneNumber = request.POST['phonenumber']
        userAddress = request.POST['address']
        userPass = request.POST['pass']
        userID = ran_gen(8,"1234567890")
        orderedProd = []
        newUser = customer(
            name = userName ,
            surname = userSurname ,
            father_name = userFatherName ,
            address = userAddress ,
            email = userEmail ,
            phone_number = userPhoneNumber ,
            password = userPass ,
            user_id = userID,
            ordered_products = orderedProd
        )
        newUser.save()
        request.session['userID']= userID
        request.session['userName'] = userName
        request.session['orderedProd'] = orderedProd
        request.session['userBalance'] = newUser.balance
        return redirect('index')
    return render(request,'signup.html')

def productsee(request,id):
    if request.method == "POST":
     if request.session.get('userID'):
        productid = request.POST['productID']
        productinfo = product.objects.all().filter(product_id=productid).values()[0]
        productquantity = int(request.POST['productQuantity'])
        if productinfo['discount']:
            productTotal = round(float(productinfo['discount'])*productquantity,2)
        else:
            productTotal = round(float(productinfo['price'])*productquantity,2)
        userid = request.session['userID']
        jsonProd = {"product":productinfo,"quantity":productquantity,'total':round(productTotal,2)}
        
        checkUserhaveBasketOrNot1 = shoppingcart.objects.all().filter(user_id=userid).values()
        if checkUserhaveBasketOrNot1:
            checkUserhaveBasketOrNot = shoppingcart.objects.get(user_id=userid)
            for producta in checkUserhaveBasketOrNot.product_id_and_quantities:
                if jsonProd['product']['product_id'] == producta['product']['product_id']:
                    producta['quantity'] +=productquantity
                    if producta['product']['discount']:
                        producta['total'] = round(producta['quantity'] * producta['product']['discount'],2)
                    else:
                        producta['total'] = round(producta['quantity'] * producta['product']['price'],2)
                    checkUserhaveBasketOrNot.save()
                    return redirect('shoppingcart')
            checkUserhaveBasketOrNot.product_id_and_quantities.append(jsonProd)
            checkUserhaveBasketOrNot.save()
            messages.success(request,'Uğurla Əlavə Olundu!')
            return redirect('shoppingcart')
        else:
            prods = '[]'
            prods = json.loads(prods)
            prods.append(jsonProd)
            newBasket = shoppingcart(
                product_id_and_quantities =prods,
                user_id = userid
            ) 
            newBasket.save()
            return redirect('shoppingcart')
     else:
        return redirect('login')
    else:
     if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
     else:
        bas = 0
     item = product.objects.all().filter(product_id=id).values()[0]
     prodct= product.objects.all().values()
     context = {
         'item':item,
        'prods':prodct,
        'basket':bas
      }
     return render(request,'shop-details.html',context)

def cart(request):
 if request.session.get('userID'):
    if request.method == "POST" and request.POST['deleteITEM']:
          product_id_to_delete = request.POST['deleteITEM']
          userCart = shoppingcart.objects.get(user_id=request.session['userID'])
          userCart.product_id_and_quantities = [item for item in userCart.product_id_and_quantities if item['product']['product_id'] != product_id_to_delete]
          userCart.save()
          return redirect('shoppingcart')
    userid = request.session['userID']
    totalcart = 0
    usercart = shoppingcart.objects.all().filter(user_id=userid).values()
    for product in usercart:
        for prod in product['product_id_and_quantities']:
            totalcart+=prod['total']
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    context = {

        'cartproducts':usercart,
        'total':round(totalcart,2),
        'basket':bas
    }
    return render(request,'shoping-cart.html',context)
 else:
   return redirect('login')
 



def userprofile(request):
 if request.session.get('userID'):
    if request.method == "POST":
         username = request.POST['userName']
         usersurname = request.POST['userSurname']
         userFather = request.POST['fatherName']
         userAddress = request.POST['userAddress']
         userMail = request.POST['userEmail']
         userPhone = request.POST['userNumber']
         userPass = request.POST['userPassword']
         userNewPass = request.POST['userNewPassword']
         useridd = request.session['userID']
         userChanges = customer.objects.get(user_id=useridd)
         if userChanges.password == userPass:
          userChanges.name = username
          userChanges.surname = usersurname
          userChanges.father_name = userFather
          userChanges.address = userAddress
          userChanges.email = userMail
          if len(userNewPass)>0:
            userChanges.password = userNewPass
          userChanges.save()
          messages.success(request,'Changed Successfully!')
         else:
            messages.error(request,'Old Password Is Wrong!')
         return redirect('profile')
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    usercontent = customer.objects.get(user_id=request.session.get('userID'))

    context = {
        'basket':bas,
        'name':usercontent.name,
        'surname':usercontent.surname,
        'father':usercontent.father_name,
        'address':usercontent.address,
        'email':usercontent.email,
        'phone':usercontent.phone_number,
        'userid':usercontent.user_id
    }
    return render(request,'profileinfo.html',context)
 else:
    return redirect('login')
 
def checkout(request):
 if request.session.get('userID'):
   if request.method == "POST":
    
       user_product_and_quantities = shoppingcart.objects.all().filter(user_id=request.session['userID']).values()[0]['product_id_and_quantities']
       additional_note = request.POST['addNotes']
       endpoint_secret = 'sk_test_51M1aAoJilhQEZGyd2yLJw9XO6RdljJyJTLy3gz2alTBpaGsP4nOvUc4zqwfUUa8gvlnBpynDKxVAYab6cuAmxesp00lIXCx44G'
       total = request.POST['totalPayment']
       total_new = ''
       for i in total:
          if i == ',':
             total_new+='.'
          else:
             total_new+=i
             
       total = float(total_new)
       hostName = request.META['HTTP_HOST']
       if request.POST['payType'] == 'card':
          newPay  =stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'azn',
        'product_data': {
          'name': 'Payment',
        },
        'unit_amount': int(round(total*100,2)),
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url=f'http://{hostName}/proccesing',
    cancel_url=f'http://{hostName}/failure',
  )
          newOrder = order(
           order_id = ran_gen1(15, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"),
           order_total_payment = float(total),
           payment_id = newPay.id,
           payment_date = datetime.now(),
           product_id_and_quantities = user_product_and_quantities,
           user_id = request.session['userID'],
           additional_notes = additional_note
       )
         
          deleteSc = shoppingcart.objects.get(user_id=request.session['userID'])
          deleteSc.delete()
          request.session['pay_id'] = newPay.id
          newOrder.save()
          return redirect(newPay.url)
       elif request.POST['payType'] == 'balance':
          if total>request.session['userBalance']:
             return redirect('failure')
          else:
             user = customer.objects.get(user_id=request.session['userID'])
             balanceafter = round(request.session['userBalance'] - total,2) 
             user.balance = balanceafter
             carts = shoppingcart.objects.get(user_id=request.session['userID'])
             carts.delete()
             request.session['userBalance'] = user.balance
             user.save()
             newOrder = order(
           order_id = ran_gen1(15, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"),
           order_total_payment = float(total),
           payment_id = 'balance_paid',
           payment_son = True,
           product_id_and_quantities = user_product_and_quantities,
           user_id = request.session['userID'],
           additional_notes = additional_note
       )
             newOrder.save()
             return redirect('success')
   products = shoppingcart.objects.filter(user_id=request.session['userID']).values()
   totalcart = 0
   try:
    for prod in products[0]['product_id_and_quantities']:
        totalcart += prod['total']
   except IndexError:
        totalcart = 0
   if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
   else:
        bas = 0
   
   context = {
      'products':products,
      'total':totalcart,
      'basket':bas
   }
   return render(request,'checkout.html',context)
 else:
    return redirect('login')
def userorders(request):
 if request.session.get('userID'):
    userOrders = order.objects.all().filter(user_id=request.session['userID']).values()
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    context = {
        'userorders':userOrders,
        'basket':bas
    }
    return render(request,'orders.html',context)
 else:
    return redirect('login')

    
    

def successpay(request):
 if request.session.get('userID'):
  return render(request,'success.html')
 else:
    return redirect('login')

def failure(request):
 if request.session.get('userID'):
    return render(request,'failure.html')
 else:
    return redirect('login')


def getorderdat(request,id):
    userOrder = order.objects.get(order_id=id)
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
   
    context = {
        'order':userOrder,
        'basket':bas
    }
    return render(request,'orderdetails.html',context)

def addbalance(request):
 if request.session.get('userID'):
    if request.method == "POST":
        balanceWant = round(float(request.POST['addCost']),2)
        user = customer.objects.get(user_id=request.session['userID'])
        hostName = request.META['HTTP_HOST']
        new_pay_session = stripe.checkout.Session.create(
            line_items=[{
      'price_data': {
        'currency': 'azn',
        'product_data': {
          'name': 'Payment',
        },
        'unit_amount': int(round(balanceWant*100,2)),
      },
      'quantity': 1,
    }],
            mode='payment',
            success_url=f'http://{hostName}/proccesing',
            cancel_url=f'http://{hostName}/failure',
            payment_method_types = ['card']
        )
        request.session['pay_balance_id'] = new_pay_session.id
        return redirect(new_pay_session.url)
    if shoppingcart.objects.all().filter(user_id=request.session.get('userID')):
        bas = len(shoppingcart.objects.get(user_id=request.session.get('userID')).product_id_and_quantities)
    else:
        bas = 0
    context = {
       'basket':bas
    }
    return render(request,'addbalance.html',context)
 else:
    return redirect('login')

def check_payment(request):
  render(request,'proccess.html')
  time.sleep(20)
  if request.session.get('userID'):
   
   if request.session.get('pay_id'):
    checkPay = order.objects.get(payment_id = request.session['pay_id'])
    pay_status = stripe.checkout.Session.retrieve(request.session['pay_id'])
    request.session['pay_id'] = ''
    if pay_status['payment_status'] == 'paid':
       checkPay.payment_son = True
       checkPay.save()
       return redirect('success')
    else:
        checkPay.delete()
        return redirect('failure')
   elif request.session.get('pay_balance_id'):
    checkPay = stripe.checkout.Session.retrieve(
       request.session['pay_balance_id']
    )
    request.session['pay_balance_id'] = ''
    if checkPay['payment_status'] == 'paid':
     paycost = checkPay['amount_subtotal'] / 100
     user = customer.objects.get(user_id=request.session['userID'])
     user.balance += paycost
     request.session['userBalance']= round(user.balance,2)
     user.save()
     return redirect('success')
    else:
       return redirect('failure')
   else:
      return render(request,'404.html')
  else:
     return redirect('login')