
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
    search_view,
    posts_by_tag
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
    path("post/<int:pk>/comments/new/",CommentCreateView.as_view(),name="comment-create"),
    path("comment/<int:pk>/update/",CommentUpdateView.as_view(),name="comment-update"),
    path("comment/<int:pk>/delete/",CommentDeleteView.as_view(),name="comment-delete"),
    path("search/", search_view, name="search"),
    path("tags/<str:tag_name>/", posts_by_tag, name="posts-by-tag"),
]