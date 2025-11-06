# CRUD Operations Summary

This document aggregates the Create, Retrieve, Update, and Delete operations performed in the Django shell on the `Book` model.

---

## Create Operation

```python
# Open Django shell
python manage.py shell

# Create a Book instance
from library.models import Book

x = Book(title="1984", author="George Orwell", publication_year=1949)
x.save()
x
```

**Expected Output:**

```
<Book: 1984 by George Orwell (1949)>
```

---

## Retrieve Operation

```python
# Retrieve and display all attributes of the created book
from library.models import Book

Book.objects.all().values()

```

**Expected Output:**

```
1984 George Orwell 1949
```

---

## Update Operation

```python
# Update the title of the book
from library.models import Book

book = Book.objects.all()[0]
book.title = "Nineteen Eighty-Four"
book.save()
book
```

**Expected Output:**

```
Nineteen Eighty-Four
```

---

## Delete Operation

```python
# Delete the book and confirm deletion
from library.models import Book

book = Book.objects.all()[0]
book.delete()
Book.objects.all()
```

**Expected Output:**

```
<QuerySet []>
```
