from rest_framework import serializers

from app.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors", "pic")
        extra_kwargs = {
            'book_name': {
                'required': True,
                'min_length': 2,
                'error_message': {
                    'required': '图书名必须提供',
                    'min_length': '图书名不能少于两个字',
                }
            },
            'pic': {
                'read_only': True
            },
            'publish': {
                'write_only': True
            },
            'authors': {
                'write_only': True
            },
        }

    def validate(self, attrs):
        return attrs

    def validate_book_name(self, value):
        return value
