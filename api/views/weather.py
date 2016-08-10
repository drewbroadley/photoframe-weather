# http://www.metservice.com/publicData/localForecastlower-hutt
# http://www.metservice.com/publicData/localObs_lower-hutt

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
#from django.http import HttpResponse
import requests
from django.conf import settings
import os, random

class WeatherView(APIView):
    """
    View random photo
    """

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        """
        Return next photo.
        """

        weather_forecast = requests.get('http://www.metservice.com/publicData/localForecastlower-hutt').json()
        weather_observation = requests.get('http://www.metservice.com/publicData/localObs_lower-hutt').json()

        weather = {
            'info': weather_observation.get('threeHour'),
            'forecast': {
                'today': weather_forecast.get('days', [])[0],
                'tomorrow': weather_forecast.get('days', [])[1]
            }

        }

        return Response(weather)

        #print(":D")
        #photo
        #return ExtendedJsonResponse(content, request=request, status=status.HTTP_200_OK).render()