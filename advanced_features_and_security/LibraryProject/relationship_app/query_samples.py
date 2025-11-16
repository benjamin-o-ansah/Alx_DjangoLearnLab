from relationship_app.models import Author, Book, Library, Librarian



def insert_sample_data():
# Create authors
    a1 = Author.objects.create(name="J.K. Rowling")
    a2 = Author.objects.create(name="George R.R. Martin")

    # Create books
    b1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=a1)
    b2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=a1)
    b3 = Book.objects.create(title="A Game of Thrones", author=a2)

    # Create libraries
    lib1 = Library.objects.create(name="Central Library")
    lib2 = Library.objects.create(name="Community Library")

    # Add books to libraries
    lib1.books.add(b1, b3)
    lib2.books.add(b2)

    # Create librarians
    Librarian.objects.create(name="Alice", library=lib1)
    Librarian.objects.create(name="Bob", library=lib2)

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return author,books
   

# 2️⃣ List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all().values()
    
    
# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Librarian.objects.get(library=library_name)
   

def get_all_books():
    books = Author.objects.all().values()
    return books

# 2️⃣ List all books in a specific library
def get_all_libraries():
    all_libraries = Library.objects.all().values()
    return all_libraries
    
# 3️⃣ Retrieve the librarian for a library
def get_all_libranians():
    librarians = Librarian.objects.all().values()
    return librarians
