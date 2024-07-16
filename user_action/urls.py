from django.urls import path
from .views import action_list, post_detail, like_post, unlike_post, add_comment, like_comment, unlike_comment, delete_comment

urlpatterns = [
    path('', action_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike_post'),
    path('<int:pk>/comment/', add_comment, name='add_comment'),
    path('comment/<int:pk>/like/', like_comment, name='like_comment'),
    path('comment/<int:pk>/unlike/', unlike_comment, name='unlike_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
]
