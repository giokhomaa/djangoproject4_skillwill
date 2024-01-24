from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, default="Name")
    surname = models.CharField(max_length=100, default='surname')
    personal_thoughts = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=100, default='Title')
    description = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, default='Genre')
    release_date = models.DateTimeField()
    personal_thoughts = models.TextField()