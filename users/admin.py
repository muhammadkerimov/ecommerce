from django.contrib import admin
from .models import  comment , payment , customer , product , review , categories

admin.site.register(comment)
admin.site.register(payment)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(review)
admin.site.register(categories)