from django.urls import path
from . import views


urlpatterns = [
    path('memes/', views.memes, name='memes'),
    path('meme/<str:pk>/', views.meme, name='meme'),

    path('upload_meme/', views.uploadMeme, name='upload_meme'),
    path('update-meme/<str:pk>', views.updateMeme, name="update-meme"),
    path('delete-meme/<str:pk>/', views.deleteMeme,
         name="delete-meme"),
    path('smiley-meme/<str:pk>/', views.likeMeme, name="smiley-meme"),
]
