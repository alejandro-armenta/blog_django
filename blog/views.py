from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator


def post_detail(request, year, month, day, post):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )

    return render(request, "blog/post/detail.html", {"post": post})


def post_list(request):

    post_list = Post.published.all()

    paginator = Paginator(post_list, 3)

    number = request.GET.get("page", 1)

    posts = paginator.page(number)

    return render(request, "blog/post/list.html", {"posts": posts})
