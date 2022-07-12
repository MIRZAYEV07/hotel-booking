from django.contrib import admin
from .models import Category , Hotel , HotelRoom

class HotelAdmin(admin.ModelAdmin):
    exclude = ['created_date','updated_date']

class RoomAdmin(admin.ModelAdmin):
    exclude = ['created_date','updated_date']

admin.site.register(Category)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(HotelRoom,RoomAdmin)
