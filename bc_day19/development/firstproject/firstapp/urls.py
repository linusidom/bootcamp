from django.urls import path
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path('create', views.BlogCreateView.as_view()),

    # Generic detail view BlogUpdateView must be called with either an 
    # object pk (Number) 
    # or a slug (string) in the URLconf.
    path('update/<int:pk>/', views.BlogUpdateView.as_view()),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view()),
]
