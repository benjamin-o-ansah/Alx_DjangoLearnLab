from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .query_samples import insert_sample_data, getAllBooks, get_all_libraries, get_all_libranians,get_all_authors
from django.template import loader
from .models import Library,Librarian,Author,Book


def display_all(request):
    insert_sample_data()
    if(insert_sample_data):
        print('Sample data inserted successfully.')
    else:
        print('Sample data insertion failed or already exists.')
    books = getAllBooks()
    libraries = get_all_libraries()
    librarians = get_all_libranians()
    authors = get_all_authors()
    # template = loader.get_template('index.html')
    context = {
        'books': books,
        'libraries': libraries,
        'librarians': librarians,
        'authors': authors,
    }
    return render(request,'library_detail.html', context)

def list_books(request):
    books = Book.objects.all().values()
    # template = loader.get_template('list_books.html')
    context = {
        'books': books,
    }   
    return render(request,'relationship_app/list_books.html',context)

class LibraryDetailView(DetailView):
    """Display details for a specific library and its books."""
    model = Library
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Optional: prefetch related books for performance
        context['books'] = self.context_object_name.object.books.select_related('author').all()
        template = loader.get_template('relationship_app/library_detail.html')
        return HttpResponse(template.render(context,self.request))

def register_view(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            login(request, user)  # Auto-login after registration
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# ----------------------------
# User Login View
# ----------------------------
def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('list_books')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# ----------------------------
# User Logout View
# ----------------------------
def logout_view(request):
    """Handle user logout."""
    logout(request)
    return render(request, 'relationship_app/logout.html')