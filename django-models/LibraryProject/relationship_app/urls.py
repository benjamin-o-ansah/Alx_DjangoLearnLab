from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.display_all, name='display_all'),
]