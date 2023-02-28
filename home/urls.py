
from django.contrib import admin
from django.urls import path
from home import views
from .views import *

urlpatterns = [
    path("",views.index,name='home'),
    path("topplaces",views.topplaces,name='Top Places'),
    path("hotel",views.hotel,name='hotels'),
    path("contact",views.contact,name='contact'),
    path("places",views.places,name='places'),
    path("signup",views.signup,name='signup'),
    path("login",views.login,name='login'),
    path("signout",views.signout,name='signout'),
    
]