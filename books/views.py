from django.shortcuts import render,redirect

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm



def book_list(request):
    query = request.GET.get('q')
    genre = request.GET.get('genre')
    sort_by = request.GET.get('sort_by')
    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)
    if genre:
        books = books.filter(genre=genre)
    if sort_by:
        books = books.order_by(sort_by)

    paginator = Paginator(books, 6)  # Show 6 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_list.html', {'page_obj': page_obj})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})
