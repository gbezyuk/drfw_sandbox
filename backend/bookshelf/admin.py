from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Author, Publisher, Book


class AuthoredBookInline(admin.TabularInline):
    model = Book
    fk_name = 'author'
    verbose_name = _('authored book')
    verbose_name_plural = _('authored books')


class CoauthoredBookInline(admin.TabularInline):
    model = Book
    fk_name = 'coauthor'
    verbose_name = _('coauthored book')
    verbose_name_plural = _('coauthored books')


class PublishedBookInline(admin.TabularInline):
    model = Book
    fk_name = 'publisher'
    verbose_name = _('published book')
    verbose_name_plural = _('published books')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = (AuthoredBookInline, CoauthoredBookInline)
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = (PublishedBookInline,)
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'coauthor', 'publisher', 'year')
    list_display_links = ('id', 'title', 'author', 'coauthor', 'publisher', 'year')
    list_filter = ('author', 'coauthor', 'publisher', 'year')
    search_fields = ('title', 'author__first_name', 'author__last_name',
                     'coauthor__first_name', 'coauthor__last_name',
                     'publisher__name', 'year')
