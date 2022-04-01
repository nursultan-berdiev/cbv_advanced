from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('detail/<int:id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('test/', views.test_list_view, name='test'),
    path('comment/', views.comment_list_view, name='comment'),
]