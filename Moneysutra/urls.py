"""
URL configuration for Moneysutra project.

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
from django.urls import path
from Apps import views

admin.site.site_header = "MONEY SUTRA PERSONAL"
admin.site.site_title = "WELCOME TO MONEY SUTRA LOAN WEBSITE ADMIN PAGE"
admin.site.index_title = "WELCOME TO MONEY SUTRA"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name='home'),
    path('base/',views.base),
    path('',views.homepage),
    path('contactus/',views.contactus,name='contactus'),
    path('service/',views.service),
    path('aboutus/',views.aboutus),
    path('news/',views.news),
    path('login/',views.login,name='login'),
    path('learn/',views.learn),
    path('peages/',views.peages),
    path('applyloan/',views.applyloan),
    path('signup/',views.signup,name='signup'),
    path('payments/',views.payments),
    path('document/',views.document),
    path('calculoter/',views.calculoter),
    path('faqs/',views.faqs),
    path('bussiness/',views.bussiness),
    path('cibil/',views.cibil),
    path('cards/',views.cards),
    path('personal/',views.personal),
    path('banking/',views.banking),
    path('how_apply/',views.how_apply),
    path('form/',views.form,name='form'),
    path('cricket/',views.cricket),
]

