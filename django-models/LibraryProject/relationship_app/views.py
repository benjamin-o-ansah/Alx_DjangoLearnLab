
from django.http import HttpResponse
from .query_samples import insert_sample_data, get_all_books, get_all_libraries, get_all_libranians
from django.template import loader

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