from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),        # <pk> is <primary key>
    path('post/new/', PostCreateView.as_view(), name='post-create'),             # Linked to post_form.html
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),  # Linked to post_form.html
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),  # Linked to post_confirm_delete.html
    path('about/', views.about, name='blog-about'),
]
