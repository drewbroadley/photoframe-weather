from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
#from django.http import HttpResponse
from django.conf import settings
import os, random

class PhotoView(APIView):
    """
    View random photo
    """

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        """
        Return next photo.
        """
        photo = settings.PHOTO_URL_ROOT + random.choice(os.listdir(settings.PHOTO_ROOT))

        return Response(photo)

        #print(":D")
        #photo
        #return ExtendedJsonResponse(content, request=request, status=status.HTTP_200_OK).render()