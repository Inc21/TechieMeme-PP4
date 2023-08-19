from django.urls import path
from . import views


urlpatterns = [
    path('memes/', views.memes, name='memes'),
    path('meme/<str:pk>/', views.meme, name='meme'),
    path('', views.home_page, name='home_page'),

    path('upload_meme/', views.uploadMeme, name='upload_meme'),
]
