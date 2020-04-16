from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'secondapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name='secondapp/index.html'), name='index'),
]
