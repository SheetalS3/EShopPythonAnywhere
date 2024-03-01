from django.shortcuts import render, HttpResponse, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.order import Order
from store.middlewares.auth import auth_middleware


class OrderView(View):  

    # @method_decorator(auth_middleware)    #instead here you can put it in urls.py
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_id(customer)
        return render(request, "order.html", {'orders': orders})
       