from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.display_all, name='display_all'),
    path('books/', views.displayAllBooks, name='displayAllBooks'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail')
]