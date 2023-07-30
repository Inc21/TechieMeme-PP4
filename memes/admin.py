from django.contrib import admin

# Register your models here.
from .models import Meme, Review, Tag

admin.site.register(Meme)
admin.site.register(Review)
admin.site.register(Tag)
