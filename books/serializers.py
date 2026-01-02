from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ["id", "title", "subtitle", "author", "price"]

    def validate(self, data):
        title = data.get("title")
        author = data.get("author")

        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob nomi harflardan iborat bo'lishi kerak",
                }
            )

        if (
            Books.objects.filter(title=title).exists()
            and Books.objects.filter(author=author).exists()
        ):
            raise ValidationError(
                {
                    "status": False,
                    "message": "Bir hil kitobni bir hil muallif tomonidan qayta qosha olmaysiz",
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 99999999:
            raise ValidationError(
                {
                    "success": False,
                    "message": "Narx 0 va 99999999 dan oshmasligi kerak ",
                }
            )

        return price
