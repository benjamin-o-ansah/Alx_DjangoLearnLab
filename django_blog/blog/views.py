from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login

from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm,RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login') # Redirect to the login page
#     else:
#         form = CustomUserCreationForm()
    
#     context = {'form': form}
#     return render(request, 'blog/register.html', context)

def home(request):
    """
    Renders the main landing page of the blog.
    """
    # We will pass an empty context for now, but you could pass Post objects here later.
    return render(request, 'blog/home.html', {})

# @login_required 
# def profile(request):
#     if request.method == 'POST':
#         # Instantiate both forms with POST data and the existing instance data
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES, # Pass files data for the profile picture
#                                    instance=request.user.profile)
        
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile') # Redirect to GET request to avoid resubmission on refresh
            
#     else:
#         # Instantiate forms with current user data for GET request
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'blog/profile.html', context)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})