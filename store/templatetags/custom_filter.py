from django import template

register = template.Library()

   
@register.filter(name= "currency")   
def currency(number):
    return "₹" + str(number)   

@register.filter(name= "multiply")  #here we have to multipy price and quantity in order.html
def multiply(num1, num2):
    return num1*num2