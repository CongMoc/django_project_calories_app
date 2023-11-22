from django.db import models

# Create your models here.
class Information_User(models.Model):
    username = models.CharField(null=True,max_length=200)
    age = models.IntegerField(null=True,)
    gender = models.CharField(null=True,max_length=10)
    height = models.IntegerField(null=True,)
    weight = models.IntegerField(null=True,)
    food_allergies = models.CharField(null=True,max_length=20)
    time_exercise_week = models.CharField(null=True,max_length=20)
    time_exercise_day = models.CharField(null=True,max_length=20)
    category_food = models.CharField(null=True,max_length=50)
    category_exercise = models.CharField(null=True,max_length=50)
    body_condition = models.CharField(null=True,max_length=20)
    calories = models.FloatField(null=True)

    def __str__(self):
        return (f"{self.calories}")


class Food(models.Model):
    Food_Image = models.ImageField(null=True, blank=True, upload_to='images/')
    Category_Food = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.Food_Image}")

class Exercise(models.Model):
    Exercise_Image = models.ImageField(null=True, blank=True,upload_to='images/')
    Category_Exercise = models.CharField(max_length=20)
    def __str__(self):
        return (f"{self.Exercise_Image}")
