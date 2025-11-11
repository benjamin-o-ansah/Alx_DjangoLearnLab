from django.urls import path
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('display/', views.display_all, name='display_all'),
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view()),
    path('register/', views.register_view, name='register'),

    # Updated class-based views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
