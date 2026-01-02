from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {"status": "ok", "data": serializer_data}

        return Response(data=data, status=HTTP_200_OK)


# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer


class BookDetailView(APIView):

    def get(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BookSerializer(book).data
            return Response(data=serializer, status=HTTP_200_OK)
        except Exception:
            data = {"status": "False", "message": "Yuklanmadi "}
            return Response(data=data , status=HTTP_400_BAD_REQUEST)


class BookDeleteView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


# class BookCreateView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer


class BookCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": "ok", "data": serializer.data}
            print(serializer)
            return Response(data=data, status=HTTP_200_OK)
        else:
            data = {"status": "False", "message": "Yaratilmadi"}
            return Response(data=data, status=HTTP_400_BAD_REQUEST)


class BooksCreateUpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books
    serializer_class = BookSerializer


@api_view(["GET"])
def book_list_view(request):
    books = Books.objects.all()
    serializerbook = BookSerializer(books, many=True)
    return Response(serializerbook.data)


# Create your views here.
