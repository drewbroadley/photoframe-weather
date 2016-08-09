from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    # V1
    url(r'^v1/', include('api.urls_v1', namespace='v1')),

    #V2
    url(r'^v2/', include('api.urls_v2', namespace='v2')),

    # Base views
    url(r'^', include('api.urls')),
]