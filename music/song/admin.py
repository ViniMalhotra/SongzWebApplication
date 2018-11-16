from django.contrib import admin

# Register your models here.
from .models import Album, PlaySong

admin.site.register(Album)
admin.site.register(PlaySong)

