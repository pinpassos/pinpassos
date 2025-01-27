from django.contrib.auth.models import User
from django.db import models
from prose.models import Document


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True
    )

    class Meta:
        abstract = True


class Posts(TimeStampedModel):
    class StatusChoice(models.TextChoices):
        DRAFT = 'Draft'
        PUBLISHED = 'Published'
        ARCHIVED = 'Archived'

    author = models.ForeignKey(
        to=User,
        verbose_name='Author',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=200
    )
    summary = models.CharField(
        verbose_name='Summary',
        max_length=500
    )
    body = models.OneToOneField(
        verbose_name='Body',
        to=Document,
        on_delete=models.CASCADE)
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=50,
        unique=True
    )
    status = models.CharField(
        verbose_name='Status',
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.DRAFT
    )
    category = models.ForeignKey(
        to='Category',
        verbose_name='Category',
        on_delete=models.SET_NULL,
        null=True
    )
    cover_image = models.ImageField(
        verbose_name='Cover image',
        upload_to='cover-images/%Y/%m/%d/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Category(TimeStampedModel):
    name = models.CharField(
        verbose_name='Name',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=50,
        unique=True
    )
    icon_image = models.ImageField(
        verbose_name='Icon image',
        upload_to='icon-images/%Y/%m/%d/',
        blank=True,
        null=True
    )
    description = models.CharField(
        verbose_name='Description',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
