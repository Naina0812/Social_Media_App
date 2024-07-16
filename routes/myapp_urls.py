
# routes/myapp_urls.py

from django.urls import path, include

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('user_action/', include('user_action.urls')),
]
