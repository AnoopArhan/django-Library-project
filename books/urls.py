from django.urls import path
from .views import book_list, book_detail, upload_book, update_book, delete_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>/', book_detail, name='book_detail'),
    path('upload/', upload_book, name='upload_book'),
    path('<int:book_id>/update/', update_book, name='update_book'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
]