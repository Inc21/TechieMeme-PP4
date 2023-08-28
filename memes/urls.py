from django.urls import path
from . import views


urlpatterns = [
    path('memes/', views.memes, name='memes'),
    path('meme/<str:pk>/', views.meme, name='meme'),

    path('upload_meme/', views.uploadMeme, name='upload_meme'),
    path('update-meme/<str:pk>', views.updateMeme, name="update-meme"),
    path('delete-meme/<str:pk>/', views.deleteMeme,
         name="delete-meme"),
    path('smiley-face/<str:pk>/', views.smiley_face, name="smiley-face"),
    path('sad-face/<str:pk>/', views.sad_face, name="sad-face"),
    path('delete-comment/<str:pk>/', views.deleteComment,
         name="delete-comment"),
]
