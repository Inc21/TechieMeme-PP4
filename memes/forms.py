from django.forms import ModelForm
from .models import Meme, Comment
from django import forms


class MemeForm(ModelForm):
    """
    This class is used to create a form for the Meme model.
    """
    class Meta:
        model = Meme
        fields = ['meme_img', 'title', 'tags']
        labels = {
            'meme_img': 'Meme Image:',
            'title': 'Title:',
            'tags': 'Tags:'
        }

    def __init__(self, *args, **kwargs):
        super(MemeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class CommentForm(ModelForm):
    """
    This class is used to create a form for the Comment model.
    """
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': ''}

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control comment-box',
                'placeholder': 'Please leave your comment here...'})


class ReportMeme(forms.Form):
    """
    This class is used to create a form for the ReportMeme function.
    """
    name = forms.CharField(
        max_length=200, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Name*'}))
    email = forms.EmailField(max_length=200, required=True, label='',
                             widget=forms.TextInput
                             (attrs={'placeholder': 'Email*'}))
    message = forms.CharField(
        max_length=500, required=True, label='',
        widget=forms.Textarea(attrs={
            'rows': 3, 'placeholder':
                'Please describe the issue you are having with this meme...'}))

    def __init__(self, *args, **kwargs):
        super(ReportMeme, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
