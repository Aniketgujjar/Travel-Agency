from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()


   
    
class BAseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 ,editable=False,primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract=True


class Amenities(BAseModel):
    amenities_name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.amenities_name


class Hotel(BAseModel):
    hotel_name= models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)


    def __str__(self) -> str:
        return self.hotel_name

class HotelImages(BAseModel):
    hotel = models.ForeignKey(Hotel,related_name="images",on_delete=models.CASCADE)
    images = models.ImageField(upload_to = "hotel")

class HotelBooking(BAseModel):
    hotel = models.ForeignKey(Hotel,related_name="hotel_booking",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_booking",on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=100,choices=(('pre paid','pre paid'),('post paid','post paid')))
