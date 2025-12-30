from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BookSerializer


class BookListApiViews(generics.ListCreateAPIView) :
    queryset = Books.objects.all();
    serializer_class = BookSerializer
    
    


# Create your views here.
