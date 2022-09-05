from django.urls import path
from .views import index_page
from posts.views import CreatePostView, DetailPostView

urlpatterns = [
    path('', index_page, name='index'),
    path('create/post/', CreatePostView.as_view(), name='create_post'),
    path('detail/post/<int:pk>', DetailPostView.as_view(), name='detail_post'),
]
