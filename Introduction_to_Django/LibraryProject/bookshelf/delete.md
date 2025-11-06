```python
# Delete the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>
```
