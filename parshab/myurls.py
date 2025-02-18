from django.urls import path
from .views import *

urlpatterns = [
    path('contact/',contact),
    path('about/',about),
    path('homee/',homee),
    path('task/',task),
    path('form/',form),
    path('task/<pk>/',mark),   # for every task, we need to create the new url and new html page.
    path('task/<pk>/edit',edit_task),
    path('task/<pk>/delete',delete_task),
]
