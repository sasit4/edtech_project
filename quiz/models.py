from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Quiz(models.Model):

    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):

    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)

    question=models.TextField()

    option1=models.CharField(max_length=200)

    option2=models.CharField(max_length=200)

    option3=models.CharField(max_length=200)

    option4=models.CharField(max_length=200)

    correct_answer=models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Result(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)

    score=models.IntegerField()

    created_at=models.DateTimeField(auto_now_add=True)