from .models import Author, Publisher, Book
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title',
                  'author', 'coauthor', 'publisher',
                  'author_id', 'coauthor_id', 'publisher_id')

    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField()
    coauthor = AuthorSerializer(read_only=True, required=False)
    coauthor_id = serializers.IntegerField(required=False, allow_null=True)
    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.IntegerField()

    def validate_author_id(self, value):
        if not Author.objects.filter(id=value).exists():
            raise serializers.ValidationError(_('author with provided id not found'))
        return value

    def validate_coauthor_id(self, value):
        if value and not Author.objects.filter(id=value).exists():
            raise serializers.ValidationError(_('coauthor with provided id not found'))
        return value

    def validate_publisher_id(self, value):
        if not Publisher.objects.filter(id=value).exists():
            raise serializers.ValidationError(_('publisher with provided id not found'))
        return value

    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        coauthor_id = validated_data.pop('coauthor_id')
        publisher_id = validated_data.pop('publisher_id ')
        author = Author.objects.get(id=author_id)
        publisher = Publisher.objects.get(id=publisher_id)
        coauthor = Author.objects.get(id=coauthor_id) if coauthor_id else None
        book = Book.objects.create(author=author, coauthor=coauthor, publisher=publisher, **validated_data)
        return book
