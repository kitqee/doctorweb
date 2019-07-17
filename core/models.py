from django.db import models

from ordered_model.models import OrderedModel


class Author(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Book(models.Model):

    title = models.CharField(max_length=255)
    annotation = models.TextField(blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='books'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class Shelf(models.Model):

    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, through='ShelfBooks')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'shelf'
        verbose_name_plural = 'shelves'


class ShelfBooks(OrderedModel):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    order_with_respect_to = 'shelf'

    def __str__(self):
        return self.book.title

    class Meta:
        ordering = ('order',)
