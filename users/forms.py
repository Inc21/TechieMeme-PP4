from django.forms import ModelForm
from .models import UserProfile


class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'user_img', 'username', 'first_name', 'last_name', 'location',
            'email', 'bio', 'social_website', 'social_github',
            'social_linkedin', 'social_facebook', 'social_youtube'
            ]
