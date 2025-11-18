from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from .models import Book
from .forms import SearchForm

def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            books = books.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query)
            )

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })
