from django.contrib import admin

# Register your models here.
from dish_server.models import Member, Club, Restaurant, Dish

admin.site.register(Member)
admin.site.register(Club)
admin.site.register(Restaurant)
admin.site.register(Dish)

