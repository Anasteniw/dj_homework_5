from django.urls import path


from measurement.views import SensorAPIView, MeasurementAPIView

urlpatterns = [
    path('sensors/', SensorAPIView.as_view()),
    path('sensors/<pk>/', SensorAPIView.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),
    path('measurements/<pk>/', MeasurementAPIView.as_view()),
    path('sensors/<pk>/', MeasurementAPIView.as_view()),

    # TODO: зарегистрируйте необходимые маршруты
]
