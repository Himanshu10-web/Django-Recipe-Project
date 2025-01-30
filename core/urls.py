"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('', Index, name ='index'),
    path('receipes/', receipes, name ='receipes'),
    path('delete_receipe/<id>/', delete_receipe, name ='delete_receipe'),
    path('update_receipe/<id>/', update_receipe, name ='update_receipe'),
    path('login_user/', login_user, name ='login_user'),
    path('register_user/', register_user, name ='register_user'),
    path('about/', About_page, name = "about"),
    path('contact/', Contact_page, name = "contact"),
    path('admin/', admin.site.urls),

    path('logout/', logout_user, name='logout_user'),
   
    
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()