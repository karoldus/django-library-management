from django.urls import path
from . import views #z obecnego katalogu

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'), # all books view
    path('books/<int:id>', views.books_id, name='books_id'), # book detail
    #path('student/', views.student, name='student'), # student profile
    path('myprofile/', views.my_profile, name='myprofile'),
    path('accounts/register/', views.register, name="register"),
]