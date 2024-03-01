from django.contrib import admin
from django.urls import path
from store.views.login import Login, logout
from store.views.signup import Signup
from store.views.homepage import Homepage
from store.views.cart import Cart
from store.views.checkout import Checkout
from store.views.order import OrderView
from store.middlewares.auth import auth_middleware


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name= 'homepage'),
    path('signup', Signup.as_view(), name= 'signup'),
    path('login', Login.as_view(), name= 'login'),
    path('logout', logout, name= 'logout'),
    path('cart', Cart.as_view(), name= 'cart'),
    path('check-out', Checkout.as_view(), name= 'checkout'),
    path('order', auth_middleware(OrderView.as_view()), name= 'order'),

]

