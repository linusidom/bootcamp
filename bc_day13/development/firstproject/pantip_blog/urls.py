from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'pantip_blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name='pantip_blog/index.html'), name='index'),
]
