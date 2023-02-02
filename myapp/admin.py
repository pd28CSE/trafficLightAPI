from django.contrib import admin

from .models import TrafficLight

# Register your models here.

@admin.register
class AdminTrafficLight(admin.ModelAdmin):
    model = TrafficLight

    list_display = ('text', 'islighton')