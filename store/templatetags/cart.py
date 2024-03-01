from django import template

register = template.Library()

@register.filter(name= "is_in_cart")    #@register tag ne kalat ki to filter ahe. Name= jya name ne apan tyala template madhe access karnar te name
def is_in_cart(product, cart):      #cart is a dictionary(key- productId, value-quantity)
    keys = cart.keys()              #cart madhun sagale product ids ale
    for p_id in keys:
        if int(p_id) == product.id:
            return True
    return False
   
@register.filter(name= "quantity_in_cart")   
def quantity_in_cart(product, cart):
    keys = cart.keys()
    for p_id in keys:
        if int(p_id) == product.id:
            return cart.get(p_id)
    return 0    

@register.filter(name= "price_total")   
def price_total(product, cart):             #filter for calculating total price of products from cart
    return product.price * quantity_in_cart(product, cart) #varch function call karun tyala prod ani cart send

@register.filter(name= "total_cart_price")
def total_cart_price(products, cart):
    total = 0
    for p in products:
        total += price_total(p, cart) # aplyala price add karun ji total ali tyachi total karaychi ahe
    return total    


