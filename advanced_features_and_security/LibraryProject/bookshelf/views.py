from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q
from .models import Book
from .forms import SearchForm
from .forms import ExampleForm



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

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process data safely
            return render(request, 'bookshelf/form_success.html', {'form': form})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
