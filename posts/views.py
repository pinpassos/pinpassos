from django.core.paginator import Paginator
from django.shortcuts import render

from posts.models import Category, Posts


def index(request, category_id=None):
    if not category_id:
        posts = Posts.objects.all().order_by('-created_at')
    else:
        posts = Posts.objects.filter(
            category=category_id).order_by('-created_at'
        )

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'posts/index.html', context)
