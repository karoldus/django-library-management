from django.shortcuts import get_object_or_404, render

from .models import BookType, Book

# Create your views here.
def home(request):
    return render(request, "library_app/home.html", {})

def books(request):
    ls = BookType.objects.all()
    return render(request, "library_app/books.html", {"ls":ls})

def books_id(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "library_app/books_id.html", {'book':book})