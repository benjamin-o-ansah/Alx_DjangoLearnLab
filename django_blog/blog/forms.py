from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile,Post,Comment

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # Use the standard User model
        model = User 
        # Include all default fields (username, password, password2) and the email field
        fields = ('username', 'email', 'first_name', 'last_name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]

class UserUpdateForm(forms.ModelForm):
    # Make email a visible field
    email = forms.EmailField() 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] # Add more base

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content.strip()) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content
