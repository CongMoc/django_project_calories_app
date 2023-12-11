from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Information_User,Food, Exercise, User
from .forms import SignUpForm, AddInformationToPrediction
from .GradientDescent import input


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have been logging in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in. Please try again...')
            return redirect('home')
    else:
        name = request.user.username
        try:
            user_instance = User.objects.get(username=name)
        except User.DoesNotExist:
            user_instance = None 
        try:
            calories = Information_User.objects.get(user=user_instance)
            return render(request, "main/home.html",{'calories':calories})
        except Information_User.DoesNotExist:
            return render(request, "main/home.html",{'user_instance':user_instance})
    
def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authendicated and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user  = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request,"You have successfully register!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'main/register.html',{'form': form})
    return render(request, 'main/register.html',{'form': form}) 

def prediction(request):
    if request.user.is_authenticated:
        try:
            user_profile = Information_User.objects.get(user=request.user)
        except Information_User.DoesNotExist:
            user_profile = None
        username = request.user.username
        form = AddInformationToPrediction(request.POST or None,instance=user_profile)
        if request.method =='POST':
            if form.is_valid():
                if user_profile is None:
                    user_profile = form.save(commit=False)
                    user_profile.user = request.user
                else:
                    form.save()
                user_profile.body_condition, user_profile.calories = input(user_profile.gender,user_profile.height,user_profile.weight,user_profile.age, user_profile.time_exercise_week)
                user_profile.save()
                messages.success(request,'Prediction successfully')
                return redirect('home')
            else:
                form = AddInformationToPrediction(instance=user_profile)
        return render(request, 'main/prediction.html',{'form':form})
    else:
        messages.success(request,'You must to logged in...')
        return redirect('home')

def calculate_calories(request):
#5QUim0fmhRnO7Es4SKEUqw==anhQo8BB2rfK8yJR
# Create your views here.
    import requests
    import json
    if request.method =="POST":
        query = request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query,headers = {'X-Api-Key':'5QUim0fmhRnO7Es4SKEUqw==anhQo8BB2rfK8yJR'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request,'main/calculate_calo.html',{'api':api})
    else:
        return render(request,'main/calculate_calo.html',{'query':'Enter a valid query'})

def about(request):
    return render(request, "main/about.html",{})

def food(request):
    if request.user.is_authenticated:
        try:
            user_profile = Information_User.objects.get(user=request.user)
        except Information_User.DoesNotExist:
            user_profile = None
        username = request.user.username
        if user_profile == None:
            foods = Food.objects.all()
            return render(request,'main/food.html',{'food':foods})
        else:
            calories = calories_to_target(user_profile.calories);
            target = user_profile.target;
            if target == "Loss weight":
                foods = Food.objects.filter(categoryFood__lt =calories)
            else: 
                foods = Food.objects.filter(categoryFood__gte=calories)
            return render(request,'main/food.html',{'food':foods})
    else:
        messages.success(request,'You must to logged in...')
        return redirect('home')
       

def calories_to_target(calories):
    if (calories > 1200 and calories <1500):
        calories = 0;
    elif (calories >= 1500 and calories < 1700):
        calories = 1;
    elif (calories >= 1700 and calories < 1900):
        calories = 2;
    elif (calories >= 1900 and calories < 2100):
        calories = 3;
    else:
        calories = 4;
    return calories

       

def exercise(request):
    return render(request, "main/exercise.html",{})