from django.contrib import admin
from .models import Author, Publisher, Book


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = (BookInline,)
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = (BookInline,)
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher',)
    list_display_links = ('id', 'title', 'author', 'publisher',)
    list_filter = ('author', 'publisher')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'publisher__name')
