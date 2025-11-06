# Retrieve Operation

```python
# Open Django shell
python manage.py shell

# Retrieve and display all attributes of the created book
from bookshelf.models import Book

Book.objects.all().values()

```

```python
# Expected Output
<Book: 1984 by George Orwell (1949)>
```
