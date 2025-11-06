# Update Operation

```python
# Open Django shell
python manage.py shell

# Update the title of the book
from library.models import Book

book = Book.objects.all()[0]
book.title = "Nineteen Eighty-Four"
book.save()
book
```

```python
# Expected Output
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```
