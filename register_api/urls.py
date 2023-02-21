from django.urls import path, include
from rest_framework import routers
from .views import WorkList, ArtistList, register_user

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/artists/', ArtistList.as_view(), name='artist-list'),
    path('api/register/', register_user, name='register'),
]
