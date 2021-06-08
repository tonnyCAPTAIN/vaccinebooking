from django import forms
from django.forms import ModelForm
from .models import Book,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    #birthdate = forms.DateField(help_text='Required. Format: YYYY-MM-DD')


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class BookForm(ModelForm):  
    class Meta:
        model = Book
        fields = '__all__' 


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',) 


# class DateForm(forms.Form):
#     date = forms.DateTimeField(input_formats=['%d/%m/%/Y %H:M'])