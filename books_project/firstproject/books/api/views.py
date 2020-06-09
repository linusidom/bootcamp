from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from books.models import Book
from books.api.serializers import BookSerializer

class BookListAPIView(ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BookDetailAPIView(RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookCreateAPIView(CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookUpdateAPIView(UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookDeleteAPIView(DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

