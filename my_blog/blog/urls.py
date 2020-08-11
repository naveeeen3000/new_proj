from django.urls import path
from blog import views


urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('new_post',views.PostCreateView.as_view(),name='new_post'),
    path('post_detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('new_post/<int:pk>', views.post_publish, name='post_publish'),
    path('drafts/',views.DraftListView.as_view(), name='drafts'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name='post_update'),
    path('confirm_delete/<int:pk>/',views.PostDeleteView.as_view(),name='post_delete'),
    path('added/<int:pk>/',views.add_comment_to_post,name='add_comment'),
    path('comment_approved,<int:pk>/',views.approve_comment,name='approve'),
    path('comment_deleted/<int:pk>/', views.delete_comment,name='delete'),
]
