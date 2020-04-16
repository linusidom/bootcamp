from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'firstapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name='firstapp/index.html'), name='index'),
]
