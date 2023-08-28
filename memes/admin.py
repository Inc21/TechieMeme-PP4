from django.contrib import admin

# Register your models here.
from .models import Meme, Tag, Comment, ContactForm

admin.site.register(Meme)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(ContactForm)
