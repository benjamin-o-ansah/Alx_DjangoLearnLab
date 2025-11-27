from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# --- Book List and Create View (ListCreateAPIView) ---
class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles GET (list all books) and POST (create a new book) requests.
    
    Configuration:
    - queryset: Defines the set of books to retrieve.
    - serializer_class: Specifies the BookSerializer for data handling.
    
    Permissions:
    - GET (List): Allowed by anyone (IsAuthenticatedOrReadOnly).
    - POST (Create): Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom Permission Setup:
    # Allows read operations (GET, HEAD, OPTIONS) for unauthenticated users,
    # but write operations (POST, PUT, PATCH, DELETE) only for authenticated users.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Custom Behavior: Associate the Book with the currently logged-in Author/User.
    # Note: Assuming a one-to-one link between User and Author model. 
    # For simplicity here, we'll assign the Author based on the request user's ID.
    # A more robust solution would involve linking the User model to the Author model.
    # For now, we will assume the request data includes the 'author' ID.
    # We will rely on the serializer's `read_only_fields = ['author']` setting 
    # and not override `perform_create` here to keep it simple, letting the client 
    # provide the author ID during creation (for unauthenticated scenarios).
    # If the author was determined by the user, we would use:
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user.author)
    

# --- Book Detail View (RetrieveUpdateDestroyAPIView) ---
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve single book), PUT (update), PATCH (partial update), 
    and DELETE (destroy) requests for a specific book by its primary key (pk).
    
    Configuration:
    - queryset: Required to perform lookups.
    - serializer_class: Specifies the BookSerializer.
    - lookup_field: Defaults to 'pk' but can be changed (e.g., 'slug').
    
    Permissions:
    - GET (Retrieve): Allowed by anyone (IsAuthenticatedOrReadOnly).
    - PUT/PATCH (Update) & DELETE (Destroy): Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom Permission Setup (same as list/create view):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Customization: Restricting Update/Delete to the book's author (optional, but good practice).
    # For simplicity, we stick to the IsAuthenticatedOrReadOnly global check here.
    # A custom permission class (e.g., IsOwnerOrReadOnly) would be required for author restriction.