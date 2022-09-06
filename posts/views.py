from unicodedata import name
from django.shortcuts import render
from posts.models import Post
from django.views import generic
from posts.forms import CreatePostForm
from django.urls import reverse
from django.db.models import Q


def index_page(request):
    title = request.GET.get('title')
    posts = Post.objects.all()
    if title:
        posts = Post.objects.filter(Q(name__icontains=title) | Q(
            description__icontains=title))
    return render(request, 'index.html', locals())


class CreatePostView(generic.CreateView):
    template_name = 'create_post.html'
    model = Post
    form_class = CreatePostForm #to create that very form

    def get_success_url(self) -> str:
        return reverse('index')


class DetailPostView(generic.DetailView):
    template_name = 'detail_post.html'
    model = Post
    context_object_name = 'post'
