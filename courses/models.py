from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):

    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)

    instructor=models.CharField(max_length=100)

    description=models.TextField()

    price=models.IntegerField()

    image=models.ImageField(upload_to='courses')

    duration=models.CharField(max_length=100)

    video=models.FileField(upload_to='videos',null=True,blank=True)

    students=models.ManyToManyField(User,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title