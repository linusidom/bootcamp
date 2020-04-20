from django.urls import path
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    path('index', views.list_view),
    path('list', views.BlogListView.as_view()),
    path('detail/<int:pk>', views.BlogDetailView.as_view()),
    path('detail_function_based_view/<int:pk>', views.detail_view),
]
