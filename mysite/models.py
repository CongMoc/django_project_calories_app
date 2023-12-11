from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Information_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Information_User',null= True, unique=True)
    age = models.IntegerField(null=True,)
    gender = models.CharField(null=True,max_length=10)
    height = models.IntegerField(null=True,)
    weight = models.IntegerField(null=True,)
    time_exercise_week = models.CharField(null=True,max_length=20)
    time_exercise_day = models.CharField(null=True,max_length=20)
    target = models.CharField(null=True, max_length=20)
    body_condition = models.CharField(null=True,max_length=20)
    calories = models.FloatField(null=True)

    def __str__(self):
        return (f"{self.calories}")


class Food(models.Model):
    foodImage = models.ImageField(null=True, blank=True, upload_to='images/')
    categoryFood = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.Food_Image}")

class Exercise(models.Model):
    exerciseImage = models.ImageField(null=True, blank=True,upload_to='images/')
    categoryExercise = models.CharField(max_length=20)
    def __str__(self):
        return (f"{self.Exercise_Image}")
