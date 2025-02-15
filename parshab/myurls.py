from django.urls import path
from .views import contact,about,homee

urlpatterns = [
    path('contact/',contact),
    path('about/',about),
    path('homee/',homee),
]
