from django.urls import path
from . import views

urlpatterns = [
    path('holidays/', views.get_holidays, name='get_holidays'),
]
