from django.forms import ModelForm
from .models import Meme


class MemeForm(ModelForm):
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