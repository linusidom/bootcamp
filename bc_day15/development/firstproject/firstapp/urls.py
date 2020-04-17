from django.urls import path, re_path
from django.views.generic import TemplateView
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='firstapp/index.html')),
    # path('', views.index_view)
    path('list', views.BookListView.as_view(), name='list')
]