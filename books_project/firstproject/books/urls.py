from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('create', views.BookCreateView.as_view(), name='book_create'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
    
]
