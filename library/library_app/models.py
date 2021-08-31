# from typing_extensions import Required
from django.db import models

# Create your models here.
class BookType(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Book(models.Model):
    type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    production_year = models.IntegerField()
    avalible = models.BooleanField(default=True)