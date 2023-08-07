from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.userProfiles, name="user_profiles"),
    path('user/<str:pk>/', views.singleUser, name="single_user")
]
