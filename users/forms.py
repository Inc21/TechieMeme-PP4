from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import UserProfile
from memes.models import ContactForm


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


class ContactMe(ModelForm):
    """
    This class is used to create a form for the ContactForm model.
    """
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': ''
        }
        widgets = {
          'name': TextInput(attrs={'placeholder': 'Name*'}),
          'email': EmailInput(attrs={'placeholder': 'Email*'}),
          'subject': TextInput(attrs={'placeholder': 'Subject*'}),
          'message': Textarea(attrs={'rows': 4, 'placeholder': 'Message*'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactMe, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
