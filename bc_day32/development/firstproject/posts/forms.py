from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'author', 'message']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'author':forms.TextInput(attrs={'class':'form-control'}),
			'message':forms.TextInput(attrs={'class':'form-control'}),

		}