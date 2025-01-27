from django.urls import path

from posts.views import index

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', index, name='index_with_category'),
]
