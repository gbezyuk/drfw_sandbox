from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)

    @property
    def full_name(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')

    name = models.CharField(_('name'), max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        default_related_name = 'books'

    title = models.CharField(_('title'), max_length=200)
    author = models.ForeignKey(to=Author, verbose_name=_('author'))
    coauthor = models.ForeignKey(to=Author, verbose_name=_('coauthor'), blank=True, null=True,
                                 related_name='coauthored_books')
    publisher = models.ForeignKey(to=Publisher, verbose_name=_('publisher'))
    year = models.PositiveSmallIntegerField(_('year'), blank=True, null=True)

    def __str__(self):
        return self.title

