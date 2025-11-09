
from django.http import HttpResponse
from .query_samples import insert_sample_data, get_all_books, get_all_libraries, get_all_libranians
from django.template import loader
from .models import Library,Librarian,Author,Book
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404

def display_all(request):
    insert_sample_data()
    if(insert_sample_data):
        print('Sample data inserted successfully.')
    else:
        print('Sample data insertion failed or already exists.')
    books = get_all_books()
    libraries = get_all_libraries()
    librarians = get_all_libranians()
    template = loader.get_template('index.html')
    context = {
        'books': books,
        'libraries': libraries,
        'librarians': librarians,
    }
    return HttpResponse(template.render(context, request))

def displayAllBooks(request):
    books = Book.objects.all().values()
    template = loader.get_template('/relationship_app/list_books.html')
    context = {
        'books': books,
    }   
    return HttpResponse(template.render(context, request))

class LibraryDetailView(DetailView):
    """Display details for a specific library and its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Optional: prefetch related books for performance
        context['books'] = self.object.books.select_related('author').all()
        return context

