
from django.urls import path
from .views import (
    
    register_view,
    profile_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', home, name='home'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:post_id>/comments/new/",CommentCreateView.as_view(),name="comment-create"),
    path("posts/<int:post_id>/comments/<int:pk>/update/",CommentUpdateView.as_view(),name="comment-update"),
    path("posts/<int:post_id>/comments/<int:pk>/delete/",CommentDeleteView.as_view(),name="comment-delete"),
   
]