from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField(default= 0)
    description = models.CharField(max_length= 200, default= '', null= True, blank= True)
    image = models.ImageField(upload_to='uploads/products/')
    is_deleted = models.BooleanField(default= False)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default= 1)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "product"

    @staticmethod
    def get_products_by_id(ids): # ids chi list asnare 
        products = Product.objects.filter(id__in = ids)
        return products

    @staticmethod
    def get_all_products():
        return Product.objects.all()  

    @staticmethod
    def get_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)    
        else:
            return Product.get_all_products()
















