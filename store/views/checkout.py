from django.shortcuts import render, HttpResponse, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.order import Order



class Checkout(View):   
    def post(self, request):    #checkout sathi kay kay lagat te sagal get karaych
        address = request.POST.get('address')       #address form madhe submit kela ahe
        phone = request.POST.get('phone')
        customer = request.session.get('customer')  #user info i.e. customer id,  login kelyavar session madhe save keli ahe
        cart = request.session.get('cart')          # now we want product details, prod id, ani kiti quantity ahe te...te sagal cart madhun milel
        products = Product.get_products_by_id(list(cart.keys())) # cart madhalya keys mhanje pro ids, te pass kele get_prod_by_id la, so that we will get all products
        print(address, phone, customer, cart, products)

        #idea hi ahe ki, checkout kela ki sagale details order table madhe save zale pahije
        # means cart madhalya pratyek product la ek order ch obj create hoil
        #aplyala kay kay hav ahe? product, customer, quantity, price, address, phone, date automatic add hoil
        
        #product = cart chya keys madhun sagale products ale ahet

        for product in products:
            print(cart.get(str(product.id)))   #2 dictionary madhali value number ahe, ani actual quantity int so null yet ahe so convert id in str
            Order.objects.create(product = product,
                                 customer = Customer(id = customer),#cutomer= customer error, customer must be an instance
                                 quantity = cart.get(str(product.id)), #1 cart.get('product_id'), error, quantity cannot be null 
                                 price = product.price,
                                 address = address,
                                 phone = phone)

        request.session['cart'] = {}


        return redirect('cart')

