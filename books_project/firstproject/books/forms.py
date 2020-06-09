from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = []
		widgets = {
			'title': forms.TextInput(attrs={'placeholder':'Enter title','class':'form-control mt-3'}),
			'author': forms.TextInput(attrs={'placeholder':'Enter author','class':'form-control mt-3'}),
		}
		labels = {
			'title': "",
			'author': ""
		}