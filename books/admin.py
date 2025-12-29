from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin) :
    list_display = ['title' , 'author' , 'price']
    list_filter = ['price' , 'author']
    
    
admin.site.register(Books , BooksAdmin)
    

# Register your models here.
