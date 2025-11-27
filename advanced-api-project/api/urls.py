# api/urls.py

from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    # Endpoint for List (GET) and Create (POST)
    path('books/', 
         BookListCreateAPIView.as_view(), 
         name='book-list-create'),

    # Endpoint for Retrieve (GET), Update (PUT/PATCH), and Destroy (DELETE)
    path('books/<int:pk>/', 
         BookRetrieveUpdateDestroyAPIView.as_view(), 
         name='book-detail-update-destroy'),
]