from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import TrafficLight
from .serializers import TrafficLightSerializer

# Create your views here.


@api_view(['GET',])
def traffitView(request):
    trafficLight = TrafficLight.objects.get(id=1)
    serializer = TrafficLightSerializer(trafficLight, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def trafficLightOnOff(request):

    trafficLight = TrafficLight.objects.get(id=1)
    trafficLight.islighton = not (trafficLight.islighton)
    trafficLight.save()
    
    serializer = TrafficLightSerializer(trafficLight, many=False)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
