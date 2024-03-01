from typing import Any
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = "Customer"


    @staticmethod
    def get_customer_by_email(mail):
        try:
            return Customer.objects.get(email = mail)
        except Customer.DoesNotExist:
            return False