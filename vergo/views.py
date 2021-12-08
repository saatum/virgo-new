from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'vergo/home.html'
    slug_url_kwarg = 'slug'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'vergo/about.html')

def news(request):
    return render(request, 'vergo/news.html')


def services(request):
    return render(request, 'vergo/services.html')
    