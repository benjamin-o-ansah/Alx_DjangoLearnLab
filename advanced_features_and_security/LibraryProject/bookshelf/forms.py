from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        strip=True
    )
class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email'
        })
    )
    message = forms.CharField(
        required=True,
        label="Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your message'
        })
    )

