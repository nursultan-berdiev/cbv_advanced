from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
]