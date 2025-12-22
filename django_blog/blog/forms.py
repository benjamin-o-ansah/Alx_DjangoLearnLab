from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile,Post,Comment,Tag
from taggit.forms import TagWidget

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
    tags = forms.CharField(
        required=False,
        help_text="Add tags separated by commas"
         )
    class Meta:
        model = Post
        fields = ["title", "content","tags"]
        widgets = {
            "tags": TagWidget(),
        }
    
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()

        tag_names = self.cleaned_data.get("tags", "")
        tag_list = [t.strip() for t in tag_names.split(",") if t.strip()]

        post.tags.clear()
        for name in tag_list:
            tag, created = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content.strip()) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content
