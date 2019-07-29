from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
    path('', views.PostListView.as_view(), name='blog_home'),
    path('user/<str:username>/', views.AuthorPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create_post', views.PostCreateView.as_view(), name='post_create'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
]
