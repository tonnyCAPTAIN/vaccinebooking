

from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout as auth_logout 
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from book_appointment.forms import SignUpForm, BookForm, ProfileForm



def homepage(request):
    
    return render(request, 'home.html')


def login(request):
    
    if request.method=='POST':
         form = LoginForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)


            if user is not None:
                form = Loginform()
                login(request, user)

                return redirect('book')
            else:
                messages.error(request, "Invalid username or password")

            

    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', )
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("book_appointment:homepage")

#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "invalid username or password.")

#     form = AuthenticationForm()
#     return render(request=request, template_name="registration/login.html", context={"login_form":form})
        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            #user.profile.birthdate = form.cleaned_data.get('birthdate')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            #login(user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def book(request):
    print(request.user)
    #form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
           
         
            instace =form.save(commit = False)
            instace.person = request.user
            instace.save()

            messages.success(request, 'Successfully booked')

        return redirect('/book_appointment/book')   
    else:

        form = BookForm()
    
    return render(request, 'book.html', {'form':form})



def profile(request):
    #form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = request.user.profile)
        if form.is_valid():
            form.save()
        
            messages.success(request, 'Your profile has been updated!')
            
            return redirect ('/book_appointment/book')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})



def logout(request):
    auth_logout(request)
    return redirect('/book_appointment')