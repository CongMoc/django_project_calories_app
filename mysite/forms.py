from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Information_User, Food, Exercise


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    
    class Meta:
        model =User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddInformationToPrediction(forms.ModelForm):
    age = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Age","class":"form-control"}), label="")
    gender = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Gender(Male or Female)","class":"form-control"}), label="")
    height = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Height(cm)","class":"form-control"}), label="")
    weight = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Weight(kg)","class":"form-control"}), label="")
    time_exercise_week = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Time exercise in week(Example: No exercise or 1 - 3 days per week)","class":"form-control"}), label="")
    time_exercise_day =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Time exercise in day(Example: 30 minutes)","class":"form-control"}), label="")
    target = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Target(Loss weight or Build body healthy)","class":"form-control"}), label="")

    class Meta:
        model = Information_User
        fields = ['age','gender','height','weight','time_exercise_week','time_exercise_day','target']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodImage', 'categoryFood']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exerciseImage','categoryExercise']