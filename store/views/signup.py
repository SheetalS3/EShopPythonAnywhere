from django.shortcuts import render, HttpResponse, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        if request.method == "POST":
            data= request.POST
            fname = data.get('firstname')
            lname = data.get('lastname')
            ph = data.get('phone')
            mail = data.get('email')
            pwd = data.get('password')

            value = {'first_name': fname,       # field invalid asel tar, form reload karat ahot but je already entered ahe te tasech punha pass karayche so
                    'last_name': lname,
                    'phone': ph,
                    'email': mail
                    }
            customer = Customer(first_name= fname, last_name= lname, phone= ph, email= mail, password= pwd)

            error_message = self.validateCustomer(customer)
            
            #save customer
            if not error_message:
                customer.password = make_password(pwd)        #password hashing - password la encode kela ani save kela db madhe
                customer.save()
                return redirect('homepage')
            else:
                return render(request, "signup.html", {'error': error_message, 'value': value})
            
    def validateCustomer(self, customer):
        existingEmail = Customer.objects.filter(email = customer.email)   #jar email already present asel tar ithe obj return hoil
        error_message = None
        if not customer.first_name:
            error_message = "First name is required!"
        elif len(customer.first_name) > 15:
            error_message = "Number of characters should be minimum 15 in First name"
        elif not customer.last_name:
            error_message = "Last name is required!"
        elif len(customer.last_name) > 15:
            error_message = "Number of characters should be minimum 15 in Last name"
        elif not customer.phone:
            error_message = "Phone number is required!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 char long"    
        elif not customer.email:
            error_message = "Email is required!"
        elif ".com" not in customer.email:
            error_message = "Invalid Email!"
        elif not customer.password:
            error_message = "Password is required!"
        elif len(customer.password) < 4:
            error_message = "Password should not be less than 4 characters"     
        elif existingEmail:
            error_message = "Email already registered!"      
        return error_message
