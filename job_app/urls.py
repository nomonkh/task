from django.urls import path
from .views import *

urlpatterns = [
    path('executor', TaskView.as_view({'get': 'list', 'post': 'create'})),
    path('tas_create', SingleApiTask.as_view({'get': 'list', 'post': 'create'})),
]
