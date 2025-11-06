# Delete Operation

```python
# Open Django shell
python manage.py shell

# Delete the book and confirm deletion
from library.models import Book

book = Book.objects.all()[0]
book.delete()
Book.objects.all()
```

```python
# Expected Output
<QuerySet []>
```
