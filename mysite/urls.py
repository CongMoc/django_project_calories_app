from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name='index'),
    path("",views.home, name='home'),
    path("about/", views.about, name='about'),
    path("calories/", views.calories, name='calories'),
    path("food/", views.food, name='food'),
    path("exercise/", views.exercise,name='exercise'),
]