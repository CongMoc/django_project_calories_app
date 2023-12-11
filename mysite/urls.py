from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path("about/", views.about, name='about'),
    path("prediction/", views.prediction, name='add-calories'),
    path("calculate/", views.calculate_calories, name='calculate'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('exercise/', views.exercise, name='exercise'),
    path('food/', views.food, name='food'),
]