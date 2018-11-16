from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete

from song.models import Album

# By adding 'Car' as 'sender' argument we only receive signals from that model
@receiver(post_delete, sender=Album)
def on_delete(sender, **kwargs):
    instance = kwargs['instance']
    # ref is the name of the field file of the Car model
    # replace with name of your file field
    instance.album_logo.delete(save=False)





