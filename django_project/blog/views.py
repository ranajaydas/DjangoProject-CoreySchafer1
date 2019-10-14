from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Post


class PostListView(ListView):
    """Class based view for Home page."""
    model = Post
    template_name = 'blog/home.html'        # Default = <app>/<model>_<viewtype>.html
    context_object_name = 'posts'           # Variable inside the html (default = object_list)
    ordering = ['-date_posted']             # Orders the posts by newest to oldest
    paginate_by = 5                         # Number of posts per page


class UserPostListView(ListView):
    """Class based view for user post list."""
    model = Post
    template_name = 'blog/user_posts.html'  # Default = <app>/<model>_<viewtype>.html
    context_object_name = 'posts'           # Variable inside the html (default = object_list)
    paginate_by = 5                         # Number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """Class based view for individual posts."""
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Class based view for users to create new posts."""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """Required to override default form_valid method."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """Class based view for users to update their posts."""
    model = Post
    fields = ['title', 'content']
    success_message = 'Post updated!'

    def form_valid(self, form):
        """Required to override default form_valid method."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """The test that must be passed for UserPassesTestMixin

        In this case, the post author must  be one updating the post.
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """Class based view for users to delete their posts."""
    model = Post
    success_url = '/'
    success_message = "Post deleted."

    def test_func(self):
        """The test that must be passed for UserPassesTestMixin

        In this case, the post author must  be one deleting the post.
        """
        post = self.get_object()
        return self.request.user == post.author

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon post deletion."""
        messages.warning(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


def about(request):
    """Function based view for About page."""
    return render(request, 'blog/about.html', {'title': 'About'})
