from django.contrib import admin

from ordered_model.admin import (
    OrderedInlineModelAdminMixin, OrderedTabularInline
)

from core.models import Author, Book, Shelf, ShelfBooks


class BookAdmin(admin.ModelAdmin):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    model = Author


class ShelfBooksStackedInline(OrderedTabularInline):
    model = ShelfBooks
    fields = ('book', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    extra = 1
    ordering = ('order',)


class ShelfAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
    inlines = (ShelfBooksStackedInline,)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Shelf, ShelfAdmin)
