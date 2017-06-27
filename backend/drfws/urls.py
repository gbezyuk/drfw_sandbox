from django.conf.urls import url, include
from django.contrib import admin
from auth.viewsets import UserViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]
