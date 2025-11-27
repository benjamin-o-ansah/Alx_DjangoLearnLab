from rest_framework import generics, permissions, mixins
from .models import Book
from .serializers import BookSerializer

# --- DRF Generic Views using Mixins for demonstration ---

# 1. Book List and Create View (Equivalent to ListView + CreateView)
class BookListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    """
    Handles listing all books (GET) and creating a new book (POST).
    This combines the functionality of Django's ListView and CreateView for an API.
    
    Permissions: Read access for all users, Write access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        # Calls ListModelMixin.list()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Calls CreateModelMixin.create()
        return self.create(request, *args, **kwargs)


# 2. Book Detail, Update, and Destroy View (Equivalent to DetailView + UpdateView + DeleteView)
class BookRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     generics.GenericAPIView):
    """
    Handles retrieving (GET), updating (PUT/PATCH), and deleting (DELETE) a single book.
    This combines the functionality of Django's DetailView, UpdateView, and DeleteView for an API.

    Permissions: Read access for all users, Write access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        # Calls RetrieveModelMixin.retrieve()
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Calls UpdateModelMixin.update()
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Calls UpdateModelMixin.partial_update()
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        # Calls DestroyModelMixin.destroy()
        return self.destroy(request, *args, **kwargs)