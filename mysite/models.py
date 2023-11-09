from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Calories(models.Model):
    calories = models.FloatField()
    caloriesNoExercise = models.FloatField()
    caloriesExercise1to3 = models.FloatField()
    caloriesExercise4to6 = models.FloatField()
    caloriesExerciseDaily = models.FloatField()
    def __float__(self):
        return self


class User(models.Model):
    inforpassword = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    height = models.IntegerField()
    weight = models.IntegerField()
    food_allergies = models.CharField(max_length=200)
    timeExercise = models.IntegerField()
    calories = models.ForeignKey(Calories, on_delete=models.CASCADE)
    
    def __str__(self):
        return self




