"""
URL configuration for EShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  #3
from . import settings      #2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #1 static func will return one list. Apan hi list urlpatters barobar add keli

#static file - its fine if we come to know file is saved at which location
#file uploaded by user during development
# {{product.image}} as pass kela tar path jato image cha app var, end user will come to know kuthe save ahe
# so need to generate url of image {{product.image.url}}
# need to do some configurations - 
    # in urls.py + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # in settings.py add MEDIA_URL and MEDIA_ROOT
    # MEDIA_URL - 