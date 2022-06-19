from .views import ViewPosts
from django.urls import path

urlpatterns = [
    path('', ViewPosts.as_view(), name='home'),
]
