# myapp/urls.py

from django.urls import path
from .views import signup_view, login_view, follow_user, unfollow_user

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
     path('follow/<int:pk>/', follow_user, name='follow_user'),
    path('unfollow/<int:pk>/', unfollow_user, name='unfollow_user'),

]
