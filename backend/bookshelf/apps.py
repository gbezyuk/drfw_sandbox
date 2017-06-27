from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BookshelfConfig(AppConfig):
    name = 'bookshelf'
    verbose_name = _('bookshelf')
