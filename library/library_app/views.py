from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

from .models import BookType, Book

# Create your views here.
def home(request):
    return render(request, "library_app/home.html", {})

def books(request):
    ls = BookType.objects.all()
    return render(request, "library_app/books.html", {"ls":ls})

def books_id(request, id):
    book = get_object_or_404(Book, pk=id)
    if(request.POST.get('zwrot') and request.user.is_staff):
        book.borrower = None
        book.save()
    return render(request, "library_app/books_id.html", {'book':book})



@login_required
def my_profile(request):
    return render(request, "library_app/my_profile.html", {})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})