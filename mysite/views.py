from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Information_User,Food, Exercise
from .forms import SignUpForm

def home(request):
    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            infor_user = Information_User.objects.get(username=username)
            messages.success(request, 'You have been logging in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in. Please try again...')
            return redirect('home')
    else:
        return render(request, "main/home.html",{})
    
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

def about(request):
    return render(request, "main/about.html",{})

def calories(request,pk):
    return render(request,"main/calories.html",{})

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
