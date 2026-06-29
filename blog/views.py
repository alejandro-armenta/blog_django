from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm
from django.views.generic import ListView


def post_share(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )

    if request.method == "POST":
        # processing email data
        form = EmailPostForm(request.POST)

        if form.is_valid():
            ale = form.cleaned_data
    else:
        # initial form
        form = EmailPostForm()

    return render(request, "blog/post/share.html", {"post": post, "form": form})


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


class PostListView(ListView):

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_list(request):

    post_list = Post.published.all()

    paginator = Paginator(post_list, 3)

    number = request.GET.get("page", 1)

    try:
        posts = paginator.page(number)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/post/list.html", {"posts": posts})
