from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # Redirect to the login page
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'blog/register.html', context)

def home(request):
    """
    Renders the main landing page of the blog.
    """
    # We will pass an empty context for now, but you could pass Post objects here later.
    return render(request, 'blog/home.html', {})