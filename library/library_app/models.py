# from typing_extensions import Required
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class BookType(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Book(models.Model):
    type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    production_year = models.IntegerField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return f"/books/{self.id}"
    