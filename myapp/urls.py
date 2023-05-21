from .views import * 
from rest_framework import routers




router = routers.DefaultRouter()

router.register('questions', Questions, basename='questions')

urlpatterns = [
    
]+router.urls