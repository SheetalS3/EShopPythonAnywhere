from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):                    #(Get request yenya adhi konta code execute whayla pahije to)
        returnUrl=request.META['PATH_INFO']     # this will give us, from where you are redirected to the login page

        if not request.session.get('customer'): #order var click kela ani jar login nasel tar
            return redirect(f'login?return_url={returnUrl}')            # redirect to login pan with query parameters je sangtil ki after login kotya page var jaychay 
        
        response = get_response(request)
        return response

    return middleware   #decorator. returning address of wrapper function

#Built-in middlewares are created, activated by "django-admin startproject", in settings.py
#How to activate your middleware?
#    - Add entry of your middleware in that settings.py - give path from store till auth_middleware func
#        -'store.middlewares.auth.auth_middleware'
#        jar apan settings.py madhe asa activate kela tar pratyek link var mhanje pratyek request chya adhi to code run hoil
#        aplyala fakt order page la authentication dyaych ahe
    # - jar function asel tar asa decorator apply karu shakato 
    #             @auth_middleware 
    #             def get(self, request):
    #   jar method asel tar -from django.utils.decorators import method_decorator
    #             @method_decorator(auth_middleware)
    #             def get(self, request)

