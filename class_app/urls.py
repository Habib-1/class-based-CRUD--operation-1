from django.urls import path
from .views import home,createPost,edit_post,delete_post,all_post
from . import views
urlpatterns = [
   path('',home.as_view(),name='home'),
   path('create_post/',createPost.as_view(), name="create_post"),
   path('all_blog/',all_post.as_view(),name='all_post'),
   path('edit_post/<int:pk>/',edit_post.as_view(),name='edit_post'),
   path('delete/<int:pk>/',delete_post.as_view(),name='delete_post'),
]