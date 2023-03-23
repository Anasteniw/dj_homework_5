# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.response import Response
from django.core.serializers import json
from django.forms import model_to_dict
from rest_framework.generics import ListAPIView, RetrieveAPIView

# from rest_framework.views import APIView

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer


class SensorAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
   
    # создание
    def post(self, request):
        new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description'],
        )
        return Response({'new': model_to_dict(new)})

    # обновление
    def patch(self, request, pk):
        update = Sensor.objects.get(id__exact=pk)
        if 'name' in request.data:update.name = request.data['name']
        if 'description' in request.data: update.description = request.data['description']
        update.save()
        return Response({'patch': model_to_dict(update)})


class MeasurementAPIView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # измерение
    def post(self, request):
        add_temp= Measurement.objects.create(
            sensor=Measurement.objects.get(id__exact=request.data['sensor']),
            temperature=request.data['temperature'],
        )
        return Response({'Measurement': model_to_dict(add_temp)})

    # информации по датчику
    def get(self, request, pk):
        sensor_info= Sensor.objects.get(id__exact=pk)
        measures = Measurement.objects.filter(sensor_info)
        return Response(model_to_dict(measures))