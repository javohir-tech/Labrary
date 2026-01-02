from django.urls import path
from .views import (
    BookListApiView,
    BookDetailView,
    BookDeleteView,
    BookUpdateView,
    BookCreateView,
    BooksCreateUpdateDetail
)

urlpatterns = [
    path("books/", BookListApiView.as_view()),
    path("books/create/", BookCreateView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("books/<int:pk>/update/", BookUpdateView.as_view()),
    path("books/<int:pk>/delete/", BookDeleteView.as_view()),
    path("bookscreateupdatedelete/<int:pk>/" , BooksCreateUpdateDetail.as_view())
    # path('books/' , book_list_view)
]
