from django.shortcuts import render

from .models import BookType, Book

# Create your views here.
def home(request):
    return render(request, "library_app/home.html", {})

def books(request):
    ls = BookType.objects.all()
    return render(request, "library_app/books.html", {"ls":ls})

def books_id(request, id):
    return render(request, "library_app/base.html", {})