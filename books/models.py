from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    # genre = models.CharField(max_length=100)
   
    # Other fields...
    genre = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('sci-fi', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        # Add more genres as needed
    ]
    genre = models.CharField(max_length=100, choices=genre)
    published_date = models.DateField()