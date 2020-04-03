from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
	template_name = 'index.html'

class AboutTemplateView(TemplateView):
	template_name = 'about.html'

class ApparelTemplateView(TemplateView):
	template_name = 'apparel.html'

class ContactTemplateView(TemplateView):
	template_name = 'contact.html'