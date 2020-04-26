from django.shortcuts import render
from firstapp.models import Book
from django.views.generic import ListView
# Create your views here.

# def index_view(request):
# 	books = Book.objects.all()
# 	print('Type for Var \n', type(books))

# 	context = {
# 		'book_list': books
# 	}

# 	print('\nbooks for Books \n', books)

# 	for item in books:
# 		print('\n Items \n', item)

# 	return render(request, 'firstapp/index.html', context)

class BookListView(ListView):
	model = Book
	template_name = 'firstapp/index.html'
	