from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import review, aboutmovie

class registerform(UserCreationForm):
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'some',
				   'id':'uname'}))
    email = forms.EmailField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'class':'some',
				   'id':'ename'}))
    
    password1 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'some',
				   'id':'pname'}))
    password2 = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'some',
				   'id':'paname'}))

class revform(forms.ModelForm):
    
    class Meta:
        model = review
        
        field = '__all__'
        exclude = ['join', 'person']

class aboutform(forms.ModelForm):
    description = forms.CharField(max_length=1000,
                           widget= forms.TextInput
                           (attrs={'class':'some',
				   'id':'tex', 'placeholder':'Description of Movie'}))
    
    class Meta:
        model = aboutmovie
        fields = '__all__'
        exclude = ['user', 'image', 'description', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of Movie'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre of Movie'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Ratings'}),
            'link': forms.TextInput(attrs={'placeholder': 'Link To The Movie Trailer'})
        }