from django.urls import path
from .views import BookListApiView, BookDetailView, BookDeleteView, BookUpdateView

urlpatterns = [
    path("", BookListApiView.as_view()),
    path("<int:pk>/", BookDetailView.as_view()),
    path("<int:pk>/update/", BookUpdateView.as_view()),
    path("<int:pk>/delete/", BookDeleteView.as_view()),
    # path('books/' , book_list_view)
]
