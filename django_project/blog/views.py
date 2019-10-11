from django.shortcuts import render


posts = [
    {
        'author': 'Ranajay',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 11, 2019'
    },
    {
        'author': 'Pootpoot',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 10, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
