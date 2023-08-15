from django.forms import ModelForm
from .models import UserProfile


class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'user_img', 'first_name', 'last_name', 'location',
            'email', 'bio', 'social_website', 'social_github',
            'social_linkedin', 'social_facebook', 'social_youtube'
            ]
        labels = {
            'user_img': 'Profile Image:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'location': 'Location:',
            'email': 'Email:',
            'bio': 'Bio:',
            'social_website': 'Website:',
            'social_github': 'Github:',
            'social_linkedin': 'LinkedIn:',
            'social_facebook': 'Facebook:',
            'social_youtube': 'Youtube:'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
