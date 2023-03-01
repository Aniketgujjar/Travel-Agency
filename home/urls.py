
from django.contrib import admin
from django.urls import path
from home import views
from .views import *

urlpatterns = [
    path("",views.index,name='home'),
    path("topplaces",views.topplaces,name='Top Places'),
    path("hotel",views.hotel,name='hotels'),
    path("contact",views.contact,name='contact'),
    path("delhi",views.delhi,name='delhi'),
    path("vrindavan",views.vrindavan,name='vrindavan'),
    path("vaishnodevi",views.vaishnodevi,name='vaishnodevi'),
    path("agra",views.agra,name='agra'),
    path("mumbai",views.mumbai,name='mumbai'),
    path("goa",views.goa,name='goa'),
    path("jaishlmair",views.jaishlmair,name='jaishlmair'),
    path("jaipur",views.jaipur,name='jaipur'),
    path("himachal",views.himachal,name='himachal'),
    path("shimla",views.shimla,name='shimla'),
    path("lehladakh",views.lehladakh,name='lehladakh'),
    path("manali",views.manali,name='manali'),
    path("kedarnath",views.kedarnath,name='kedarnath'),
    path("signup",views.signup,name='signup'),
    path("signin",views.signin,name='signin'),
    path("signout",views.signout,name='signout'),
    
]