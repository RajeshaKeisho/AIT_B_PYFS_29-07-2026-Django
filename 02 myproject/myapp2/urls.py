from django.urls import path 
from .views import noon_message, message
urlpatterns = [
    path("noon/", noon_message, name="noon" ),
    path("message/", message, name="message" ),
]
