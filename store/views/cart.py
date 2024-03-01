from django.shortcuts import render, HttpResponse, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        return render(request, "cart.html", {'products': products})

