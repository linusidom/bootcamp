from django import forms
from firstapp.models import Blog

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'author', 'message']
	# 	widgets = {
	# 'title': forms.TextInput(attrs={'placeholder': 'Enter the Title Of your Post'}),
	# 'author' : forms.TextInput(attrs={'placeholder': 'Enter your Name'}),
	# 'message': forms.Textarea(attrs={'placeholder': 'Enter your Message'}),
	# }