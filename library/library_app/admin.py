from library_app.models import Book, BookType, Borrowing
from django.contrib import admin

# Register your models here.
admin.site.register([BookType, Book, Borrowing])
