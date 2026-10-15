from django.urls import path
from .views import employeeView

urlpatterns = [
    path("", employeeView, name='employees'),
]
