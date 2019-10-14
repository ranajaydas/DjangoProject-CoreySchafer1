from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from .models import Post


class PostListView(ListView):
    """Class based view for Home page."""
    model = Post
    template_name = 'blog/home.html'        # Default = <app>/<model>_<viewtype>.html
    context_object_name = 'posts'           # Variable inside blog/home.html (default = object_list)
    ordering = ['-date_posted']             # Orders the posts by newest to oldest


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
        """To ensure that only the author can change their own post."""
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Class based view for users to delete their posts."""
    model = Post
    success_url = '/'

    def test_func(self):
        """To ensure that only the author can change their own post."""
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    """Function based view for About page."""
    return render(request, 'blog/about.html', {'title': 'About'})
