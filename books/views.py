from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BookSerializer


class BookListApiViews(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


@api_view(["GET"])
def book_list_view(request):
    books = Books.objects.all()
    serializerbook = BookSerializer(books, many=True)
    return Response(serializerbook.data)


# Create your views here.
