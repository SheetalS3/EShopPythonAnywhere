from django.db import models
from store.models.product import Product
from store.models.customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default= 1)
    price = models.IntegerField()
    address = models.CharField(max_length= 50, default= "", blank= True)
    phone = models.CharField(max_length = 50, default= "", blank= True)
    date = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default= False)


    def __str__(self):
        return self.product.name
    
    class Meta:
        db_table = "order"

    @staticmethod
    def get_orders_by_id(customer_id):    
        return Order.objects.filter(customer = customer_id).order_by('-date') # id= nahi, customer= 

  