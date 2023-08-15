from django.urls import path
from . import views


urlpatterns = [
    path('', views.userProfiles, name="user_profiles"),
    path('user/<str:pk>/', views.singleUser, name="single_user"),

    path('update-profile/', views.updateProfile, name="update-profile"),

    path('delete-profile/<str:pk>/', views.deleteProfile,
         name="delete-profile"),
]
