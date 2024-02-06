from django.db import models
import datetime
class customer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    password = models.CharField(max_length=20)
    balance = models.FloatField(default=0)
    user_id = models.IntegerField()
    ordered_products = models.JSONField(default=None)


class product(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=3000)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='products',default=None)
    discount = models.FloatField(default=0)
    product_id = models.CharField(max_length=3000)
    comment_ids = models.JSONField()
    review_ids = models.JSONField()
    category = models.CharField(default=0,max_length=300)
    
class payment(models.Model):
    receipt = models.ImageField(upload_to='receipt')
    user_id = models.IntegerField()

class comment(models.Model):
    comment = models.CharField(max_length=3000)
    comment_owner_id = models.IntegerField()
    comment_id = models.IntegerField()


class review(models.Model):
    review = models.CharField(max_length=3000)
    review_owner_id = models.IntegerField()
    review_photos = models.ImageField(upload_to='reviews',default=None)
    review_id = models.CharField(max_length=4000,default=None)
    star_count = models.FloatField(default=0)


class shoppingcart(models.Model):
    product_id_and_quantities = models.JSONField()
    user_id = models.IntegerField()

class categories(models.Model):
    category_name = models.CharField(max_length=400)
    category_products = models.JSONField(default = dict)
    category_id = models.IntegerField()

class order(models.Model):
   product_id_and_quantities = models.JSONField(default = dict)
   order_total_payment = models.FloatField(default=0)
   order_id = models.CharField(max_length=400,default='')
   user_id = models.IntegerField()
   payment_id = models.CharField(max_length=255,default = '')
   payment_son = models.BooleanField(default=False)
   payment_date = models.DateTimeField(default=datetime.datetime.now())
   additional_notes = models.CharField(max_length=1500,default='')
   admin_delivery = models.CharField(max_length=4000,default='Waiting')
   admin_delivery_status = models.BooleanField(default=False)