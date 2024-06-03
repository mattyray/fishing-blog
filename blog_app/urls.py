# app\app.urls.py

from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new", BlogCreateView.as_view(), name="new_post"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/GoByeBye", BlogDeleteView.as_view(), name="post_delete"),
]
