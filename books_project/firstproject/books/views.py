from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from books.models import Book
from books.forms import BookForm
# Create your views here.



class BookListView(ListView):
	model = Book

	def get_context_data(self, *args, **kwargs):
		context = super(BookListView, self).get_context_data(*args, **kwargs)
		context['form'] = BookForm()
		return context


class BookDetailView(DetailView):
	model = Book

class BookCreateView(CreateView):
	model = Book
	form_class = BookForm
	success_url = reverse_lazy('books:book_list')

class BookUpdateView(UpdateView):
	model = Book
	form_class = BookForm
	success_url = reverse_lazy('books:book_list')


class BookDeleteView(DeleteView):
	model = Book
	success_url = reverse_lazy('books:book_list')

