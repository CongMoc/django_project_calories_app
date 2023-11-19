from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name='index'),
    path("",views.home, name='home'),
    path("about/", views.about, name='about'),
    path("mainCalories/", views.main, name='main'),
    path("food/", views.food, name='food'),
    path("exercise/", views.exercise,name='exercise'),
]