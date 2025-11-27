from rest_framework import serializers
from .models import Author, Book
from datetime import date

# --- BookSerializer (for use standalone and nested) ---
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['author'] # Often set when nested in AuthorSerializer

    # Custom field-level validation for publication_year
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value

# --- AuthorSerializer ---
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    **Relationship Handling:**
    It uses a nested BookSerializer to dynamically serialize all related
    Book objects for an Author. The `many=True` argument is crucial as
    an Author can have multiple Books (a one-to-many relationship).
    The field name 'books' matches the `related_name` defined in the
    ForeignKey field in the Book model (`author = models.ForeignKey(..., related_name='books')`).
    This allows the serializer to access the reverse relationship.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']