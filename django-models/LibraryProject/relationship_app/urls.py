from django.urls import path
from .views import list_books
from .import views

urlpatterns = [
    path('display/', views.display_all, name='display_all'),
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view()),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]