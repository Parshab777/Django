from django.urls import path
from .views import *

urlpatterns = [
    path('contact/',contact),
    path('about/',about),
    path('homee/',homee),
    path('task/',task),
    path('form/',form),
]
