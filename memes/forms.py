from django.forms import ModelForm
from .models import Meme, Comment


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
