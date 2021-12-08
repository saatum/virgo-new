from django.urls import path
from . views import PostListView, PostDetailView, about, news, services

urlpatterns = [
    path('about/', about, name='vergo-about'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='vergo-home'),
    path('news/', news, name='news'),
    path('services/', services, name='services'),
]
