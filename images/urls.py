from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'images'

router = SimpleRouter()
router.register('images', views.ImageViewSet, basename='images')

urlpatterns = router.urls
