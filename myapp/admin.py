from django.contrib import admin

from .models import TrafficLight

# Register your models here.

@admin.register(TrafficLight)
class AdminTrafficLight(admin.ModelAdmin):

    fields = ('text', 'islighton')
    list_display = ('text', 'islighton')