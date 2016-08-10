from django.conf.urls import url, include

from rest_framework import routers

from api.views.photo import PhotoView
from api.views.weather import WeatherView

router = routers.DefaultRouter()

urlpatterns = [
    # Base views
    url(r'^photo/$', PhotoView.as_view()),
    url(r'^weather/$', WeatherView.as_view()),
]
