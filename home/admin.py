from django.contrib import admin
from home.models import Contact,Amenities,Hotel,HotelBooking,HotelImages

# Register your models here.
admin.site.register(Contact)
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)