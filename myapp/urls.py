from django.urls import path

from . import views

urlpatterns= [ 
    path('', views.traffitView, name='traffic-light-status'),
    path('power-on-off/', views.trafficLightOnOff, name='traffic-light-power-On-Off'),
]