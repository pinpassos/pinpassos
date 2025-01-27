from django.contrib import admin

from posts.models import Category, Posts

admin.site.register([
    Posts,
    Category
])
