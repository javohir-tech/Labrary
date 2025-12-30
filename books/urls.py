from django.urls import path
from .views import BookListApiViews

urlpatterns = [
    path('books/v1/' , BookListApiViews.as_view() , name='home')
]
