<<<<<<< HEAD
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    image=models.ImageField(
        upload_to='profiles',
        default='default.png'
    )

    bio=models.TextField(blank=True,null=True)

    def __str__(self):
=======
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    image=models.ImageField(
        upload_to='profiles',
        default='default.png'
    )

    bio=models.TextField(blank=True,null=True)

    def __str__(self):
>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
        return self.user.username