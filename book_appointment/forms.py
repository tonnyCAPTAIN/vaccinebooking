from datetime import date
from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Book,Profile, Venue
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    #birthdate = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(ModelForm):  
    class Meta:
        model = Book
        fields = ['date'] 

        widgets= {
            'date': DateInput(),

        }


class Book_SecondForm(ModelForm):  
    class Meta:
        model = Book
        fields = ['date'] 

        widgets= {
            'date': DateInput(),

        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',) 


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('hospital',)