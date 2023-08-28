from django.contrib import admin

# Register your models here.
from .models import Meme, Tag, Comments, ContactEmail

admin.site.register(Meme)
admin.site.register(Comments)
admin.site.register(Tag)
admin.site.register(ContactEmail)
