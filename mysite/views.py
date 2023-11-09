from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Calories

# Create your views here.
def index(response, id):
    UserCalories = User.objects.get(id= id)
    if  UserCalories in response.user.User.all():
        if response.method == "POST":
            print(response.POST)
    return render(response, "main/base.html",{"user": UserCalories})

def home(response):
    if response.method == "POST":
        print(response.POST)
    return render(response, "main/home.html",{})


def about(response):
    if response.method == "POST":
        print(response.POST)
    else:
        return render(response, "main/about.html",{})

def exercise(response):
    if response.method == "POST":
        print(response.POST)
    return render(response,"main/exercise.html",{})

def calories(response):
    if response.method == "POST":
        print(response.POST)
    return render(response,"main/calories.html",{})

def food(response):
    return render(response,"main/food.html",{})
