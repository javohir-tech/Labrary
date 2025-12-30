from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema

class BookLstApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    


class BookDetailView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
class BookCreateView(generics.CreateAPIView) :
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
class BooksCreateUpdateDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Books
    serializer_class = BookSerializer


@api_view(["GET"])
def book_list_view(request):
    books = Books.objects.all()
    serializerbook = BookSerializer(books, many=True)
    return Response(serializerbook.data)


# Create your views here.
