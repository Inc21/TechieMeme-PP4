from django.urls import path
from . import views


urlpatterns = [
    path('memes/', views.memes, name='memes'),
    path('meme/<str:pk>/', views.meme, name='meme'),
]
