from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # Use the standard User model
        model = User 
        # Include all default fields (username, password, password2) and the email field
        fields = ('username', 'email', 'first_name', 'last_name')