from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image', 'genre', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }