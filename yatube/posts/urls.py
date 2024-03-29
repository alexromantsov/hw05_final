from django.urls import path

from .views import (index, group_posts, profile,
                    post_detail, post_edit, post_create, add_comment,
                    follow_index, profile_follow, profile_unfollow)

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('profile/<str:username>/', profile, name='profile'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('group/<slug:slug>/', group_posts, name='group_list'),
    path('create/', post_create, name='create'),
    path('posts/<int:post_id>/edit/', post_edit, name='edit'),
    path('posts/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('follow/', follow_index, name='follow_index'),
    path('profile/<str:username>/follow/', profile_follow,
         name='profile_follow'),
    path('profile/<str:username>/unfollow/', profile_unfollow,
         name='profile_unfollow'),
]
