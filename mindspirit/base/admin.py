from django.contrib import admin
from .models import Room,topic,message
# Register your models here.
admin.site.register(Room)
admin.site.register(message)
admin.site.register(topic)

