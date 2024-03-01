from django.shortcuts import render, HttpResponse, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Homepage(View):

    def post(self, request):
        product_id = request.POST.get("prodcut_id") #cart is a dictionary(key- productId, value-quantity)
        cart = request.session.get('cart')          #session madhe cart available ahe ka check
        # request.session.get("cart").clear()       
        remove = request.POST.get("remove")         # cart madhun - karnyasathi
        if cart:                                    #jar asel
            quantity = cart.get(product_id)         #tar check quantity  #1 cart madhe prod ahe ka? 
            if quantity:                            #2 jar ahe 
                if remove:                          #3 tar zero zala asel tar cart madhun remove karaycha ahe ka?
                    if quantity <= 1:
                        cart.pop(product_id)        #4 yes remoove
                    else:    
                        cart[product_id] = quantity - 1     # remove asel tar qunatity madhun 1 minus karaycha
                else:             
                    cart[product_id] = quantity + 1        #5 otherwise jar already quantity asel tar increase kara 1 ne
            else:
                cart[product_id] = 1                #1.1 jar cart madhe prod nasel tar add 1
        else:
            cart = {}                               #jar cart ch available nasel tar empty cart add kara
            cart[product_id] = 1                    # ani tyachya prod id la 1 quantity dya

        request.session['cart'] = cart              #ata cart madhe changes kele ahet so add that cart to the session again
        print(request.session['cart'])

        return redirect('homepage')
      
    def get(self, request):
        # products = Product.get_all_products()

        cart = request.session.get('cart')  #jar cookies delete kelya thar session madhe cart obj nasel tar error so adhi check karaych 
        if not cart:                        # jar nasel tar cart empty dictionary create karaychi in session
            request.session['cart'] = {}

        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_product_by_category_id(categoryID)
        else:
            products = Product.get_all_products()    
        data = {}
        data['all_products'] = products
        data['all_categories'] = categories    
        # data['cart'] = request.session['cart']
        print("User information", request.session.get("customer"))       #printing user info ji apan signup page madhe save keli hoti session madhe
        # print("User information------------", request.session.get("email"))
        return render(request, "home.html", data)
    

