from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
class Login(View):

    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, "login.html")

    def post(self, request):
        error_message = None
        if request.method == "POST":
            mail = request.POST.get("email")
            pwd  = request.POST.get("password")
            customer = Customer.get_customer_by_email(mail)
            if customer:
                flag = check_password(pwd, customer.password)
                if flag:
                    request.session['customer'] = customer.id    # customer ne login kelyavar tyacha id session madhe save kela
                    request.session['email'] = customer.email    # customer ne login kelyavar tyacha email session madhe save kela

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('homepage')
                else:
                    error_message= "Please enter valid creadentials!"
            else:
                error_message = "Please enter valid creadentials!"
            return render(request, "login.html", {'error': error_message})      
        
def logout(request):
    request.session.clear()
    return redirect('login')
