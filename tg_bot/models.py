from django.db import models
from datetime import date


choices = (
    ('busines','busines'),
    ('econom','econom'),
    ('comfort','comfort'),
)

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.FileField(upload_to='static/img')
    rating = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField('Manzil/shahar',max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    type = models.CharField(choices=choices,default='busines',max_length=32)
    price = models.CharField(max_length=256)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserRegister(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)
    user_tgID = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def is_past_due(self):
        if date.today() < self.end_day:
            return True

class TempOrder(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

class RoomImage(models.Model):
    room=models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    room_image=models.FileField(upload_to="static/img")


# Create your models here.
