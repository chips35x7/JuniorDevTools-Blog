from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create', BlogCreateView.as_view(), name='blog_create'),
    path('category', BlogCategoryListView.as_view(), name='blog_categories'),
    path('category/<int:pk>', BlogCategoryDetailView.as_view(), name='blog_category'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('<uuid:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('<uuid:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('my_blogs', MyBlogsView.as_view(), name='my_blogs'),
    path('search', SearchResultsListView.as_view(), name='search_results'),
    path('comment/<uuid:pk>/delete', CommentDeleteView.as_view(), name='comment_delete')
]