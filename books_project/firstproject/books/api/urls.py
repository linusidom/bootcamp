from django.urls import path
from books.api import views

app_name = 'books_api'

urlpatterns = [
    path('', views.BookListAPIView.as_view(), name='book_list'),
    path('create', views.BookCreateAPIView.as_view(), name='book_create'),
    path('detail/<int:pk>', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('update/<int:pk>', views.BookUpdateAPIView.as_view(), name='book_update'),
    path('delete/<int:pk>', views.BookDeleteAPIView.as_view(), name='book_delete'),
    
]
