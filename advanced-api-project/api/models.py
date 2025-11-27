from django.db import models

# Create your models here.
from django.db import models
from datetime import date # Import for model comment

# --- Author Model ---
class Author(models.Model):
    """
    Represents an Author. This model serves as the 'one' side
    of the one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# --- Book Model ---
class Book(models.Model):
    """
    Represents a Book, linked to an Author. This model is the 'many' side
    of the one-to-many relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(
        help_text=f"The year the book was published. Must not be later than {date.today().year}."
    )
    # The ForeignKey links each Book instance to one Author.
    # related_name='books' allows us to access all books of an author
    # using author_instance.books.all()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
    class Meta:
        # Ensures no two books have the same title by the same author
        unique_together = ('title', 'author')