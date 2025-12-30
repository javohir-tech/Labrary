from django.urls import path
from .views import BookListApiViews, book_list_view

urlpatterns = [
    path('' , BookListApiViews.as_view() , name='home'), 
    path('books/' , book_list_view)
]
