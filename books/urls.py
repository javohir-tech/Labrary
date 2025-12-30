from django.urls import path
from .views import (
    BookLstApiView,
    BookDetailView,
    BookDeleteView,
    BookUpdateView,
    BookCreateView,
    BooksCreateUpdateDetail
)

urlpatterns = [
    path("", BookLstApiView.as_view()),
    path("<int:pk>/", BookDetailView.as_view()),
    path("<int:pk>/update/", BookUpdateView.as_view()),
    path("<int:pk>/delete/", BookDeleteView.as_view()),
    path("books/create/", BookCreateView.as_view()),
    path("books/<int:pk>/" , BooksCreateUpdateDetail.as_view())
    # path('books/' , book_list_view)
]
