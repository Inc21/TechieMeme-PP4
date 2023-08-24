import django_filters
from .models import Meme


class memeFilter(django_filters.FilterSet):
    class Meta:
        model = Meme
        fields = '__all__'
        exclude = ['meme_img', 'date_created']
