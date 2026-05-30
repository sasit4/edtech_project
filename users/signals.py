<<<<<<< HEAD
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile

@receiver(post_save,sender=User)

def create_profile(sender,instance,created,**kwargs):

    if created:

=======
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile

@receiver(post_save,sender=User)

def create_profile(sender,instance,created,**kwargs):

    if created:

>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
        Profile.objects.create(user=instance)