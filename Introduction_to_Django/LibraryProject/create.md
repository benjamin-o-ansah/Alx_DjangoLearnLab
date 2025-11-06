# Create Operation

```python
# Open Django shell
python manage.py shell

# Create a Book instance
x = Book(title="1984", author="George Orwell", publication_year=1949)
x.save()
Book.objects().all().values()
```

```python
# Expected Output
<Book: 1984 by George Orwell (1949)>
```

```python
#
```
