
from rest_framework import status,test
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Author, Book
from datetime import date

# Define the view names based on api/urls.py
LIST_URL = reverse('book-list')
CREATE_URL = reverse('book-create')

# Helper function to get detail URLs
def detail_url(pk):
    """Return book detail URL (GET)"""
    return reverse('book-detail', args=[pk])

def update_url(pk):
    """Return book update URL (PUT/PATCH)"""
    return reverse('book-update', args=[pk])

def delete_url(pk):
    """Return book delete URL (DELETE)"""
    return reverse('book-delete', args=[pk])


class BookAPITest(test.APITestCase):
    """Test suite for the Book API endpoints."""

    def setUp(self):
        """Set up environment: client, users, author, and initial books."""
        self.client = self.client # DRF APIClient

        # Create a regular user (for authenticated tests)
        self.user = User.objects.create_user(
            username='authuser', password='testpassword'
        )
        # Create an admin user (optional, but good for testing all permissions)
        self.admin_user = User.objects.create_superuser(
            username='adminuser', password='testpassword'
        )

        # Create an Author instance required by the Book model
        self.author1 = Author.objects.create(name='Jane Austen')
        self.author2 = Author.objects.create(name='Stephen King')

        # Create initial Book instances
        self.book1 = Book.objects.create(
            title='Pride and Prejudice', publication_year=1813, author=self.author1
        )
        self.book2 = Book.objects.create(
            title='The Shining', publication_year=1977, author=self.author2
        )
        self.book3 = Book.objects.create(
            title='Sense and Sensibility', publication_year=1811, author=self.author1
        )
        
        # Test data for POST request
        self.payload = {
            'title': 'New Book Title',
            'publication_year': date.today().year,
            'author': self.author2.id, # Must include a valid Author ID
        }

    # --- PERMISSIONS TESTING ---

    def test_create_book_requires_authentication(self):
        """Test POST to /create/ fails without authentication."""
        response = self.client.post(CREATE_URL, self.payload, format='json')
        # Expect 403 Forbidden because permission_classes = [IsAuthenticated]
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_requires_authentication(self):
        """Test PUT to /update/ fails without authentication."""
        url = update_url(self.book1.id)
        response = self.client.put(url, {'title': 'New Title'}, format='json')
        # Expect 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_requires_authentication(self):
        """Test DELETE to /delete/ fails without authentication."""
        url = delete_url(self.book1.id)
        response = self.client.delete(url)
        # Expect 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_list_and_retrieve_allow_unauthenticated(self):
        """Test GET requests are allowed for unauthenticated users."""
        # Test List View
        list_response = self.client.get(LIST_URL)
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        # Test Detail View
        detail_response = self.client.get(detail_url(self.book1.id))
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)


    # --- CRUD FUNCTIONALITY TESTING (Authenticated) ---

    def test_create_book_success(self):
        """Test creating a book with valid data and authentication."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post(CREATE_URL, self.payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4) # 3 initial + 1 new
        self.assertEqual(response.data['title'], self.payload['title'])
        self.assertEqual(response.data['author'], self.payload['author'])

    def test_create_book_invalid_year_fails(self):
        """Test creating a book with a future publication year fails validation."""
        self.client.force_authenticate(user=self.user)
        invalid_payload = self.payload.copy()
        invalid_payload['publication_year'] = date.today().year + 1
        
        response = self.client.post(CREATE_URL, invalid_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check that the custom validation error is present
        self.assertIn('publication_year', response.data)
        self.assertIn('Publication year cannot be in the future', str(response.data['publication_year']))

    def test_retrieve_book_success(self):
        """Test retrieving a book by ID."""
        response = self.client.get(detail_url(self.book1.id))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['publication_year'], self.book1.publication_year)

    def test_update_book_success(self):
        """Test updating a book using PUT (full update)."""
        self.client.force_authenticate(user=self.user)
        url = update_url(self.book1.id)
        new_year = 2005
        # Note: PUT requires all required fields, but the serializer omits 'author' as read_only_fields are set.
        updated_payload = {
            'title': 'New P&P Title',
            'publication_year': new_year
        }
        
        response = self.client.put(url, updated_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'New P&P Title')
        self.assertEqual(self.book1.publication_year, new_year)

    def test_partial_update_book_success(self):
        """Test partially updating a book using PATCH."""
        self.client.force_authenticate(user=self.user)
        url = update_url(self.book1.id)
        
        response = self.client.patch(url, {'title': 'Only Title Change'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Only Title Change')
        self.assertEqual(self.book1.publication_year, 1813) # Year remains the same

    def test_delete_book_success(self):
        """Test deleting a book."""
        self.client.force_authenticate(user=self.user)
        book_id = self.book2.id
        url = delete_url(book_id)
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book_id).exists())
        self.assertEqual(Book.objects.count(), 2)

    # --- QUERY FUNCTIONALITY TESTING ---

    def test_list_filter_by_year(self):
        """Test filtering by publication_year (exact)."""
        # ?publication_year=1813
        response = self.client.get(LIST_URL, {'publication_year': 1813})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return 'Pride and Prejudice' (1813)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_list_filter_by_author_name(self):
        """Test filtering by author_name (icontains)."""
        # ?author_name=jane
        response = self.client.get(LIST_URL, {'author_name': 'jane'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return two books by Jane Austen
        self.assertEqual(len(response.data), 2)
        # Check titles are correct (P&P and S&S)
        titles = [book['title'] for book in response.data]
        self.assertIn(self.book1.title, titles)
        self.assertIn(self.book3.title, titles)

    def test_list_search_by_title_and_author(self):
        """Test searching across title and author__name fields."""
        # ?search=prejudice
        response = self.client.get(LIST_URL, {'search': 'prejudice'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)
        
        # ?search=king
        response = self.client.get(LIST_URL, {'search': 'king'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_list_ordering_by_publication_year(self):
        """Test ordering by publication_year (descending)."""
        # ?ordering=-publication_year (Most recent first)
        response = self.client.get(LIST_URL, {'ordering': '-publication_year'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles_ordered = [book['title'] for book in response.data]
        
        # Expected order: The Shining (1977), Pride and Prejudice (1813), Sense and Sensibility (1811)
        self.assertEqual(titles_ordered[0], self.book2.title)
        self.assertEqual(titles_ordered[1], self.book1.title)
        self.assertEqual(titles_ordered[2], self.book3.title)