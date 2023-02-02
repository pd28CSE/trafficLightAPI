from rest_framework import serializers

from .models import TrafficLight


class TrafficLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrafficLight
        fields = '__all__'
        read_only_fields = ['text', ]