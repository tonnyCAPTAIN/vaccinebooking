

from covid.settings import EMAIL_HOST_USER
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
import random

from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout as auth_logout 
from django.contrib.auth.decorators import login_required, user_passes_test

from book_appointment.forms import SignUpForm, BookForm, ProfileForm, VenueForm, Book_SecondForm
from .models import Book, Doctor, Profile, Venue, Book_second
from django.core.mail import  send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def homepage(request):

    user = User.objects.all()
    context = {'user':user}
    
    return render(request, 'home.html', context)


@user_passes_test(lambda u: u.is_superuser)
def doctor(request):
    doctors = Doctor.objects.all()
    
    context = {'doctors' : doctors}
    
    return render(request, 'admin.html', context)

def about(request):

    return render( request, 'about.html')

def login(request):
    
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
                
                # username = request.POST['username']
                # password = request.POST['password']

            user = authenticate(request,username=username, password=password)


            if user is not None:
                    # form = LoginForm()
                login(request, user)

                return redirect('profile/')
                
                # else:
                #     form = AuthenticationForm()
                #     messages.error(request, "Invalid username or password")
            else:
                messages.error(request, "Invalid username or password")

            

    
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {"form":form})
                 


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            

            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            

            user = authenticate(username=username, password=password)
            user.save()
            #login(user)
            messages.success(request, f'{username} Registered successfuly.')
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Information is invalid.")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required(login_url='login')
def book(request):
    doctors = Doctor.objects.all()
    venue = Venue.objects.filter(person = request.user)
    
    
    doc = random.choice(doctors)#random assignment of a doctor
    print(doc)
    
    if len(venue) > 0:
    
            ven =list(Venue.objects.filter(person = request.user).values_list('hospital', flat=True))[-1]
            print(ven)
        
        

            if request.method == 'POST':
                
                
                form = BookForm(request.POST)
                if form.is_valid():
                    date = form.cleaned_data['date']
                    
                    
                    if len(Book.objects.filter(person_id = request.user.id)) == 0:
                        print(date)
                        instace =form.save(commit = False)
                        instace.person = request.user
                        instace.save()
                        
                        dat = date.strftime("%Y-%m-%d")
                        print(dat)
                        template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat, 'doc':doc, 'ven':ven,})
                        email = EmailMessage(
                            'Thanks for booking your first dose',
                            template,
                            settings.EMAIL_HOST_USER,
                            [request.user.profile.Email],
                        )

                        email.send()
                        

                        messages.success(request, 'Successfully booked')
                    else: 
                        print(date)

                        dat = date.strftime('%b %d %Y')
                        bk = Book.objects.get(person_id = request.user.id)#.values('date')
                        form = BookForm(request.POST, instance=bk)
                        if form.is_valid():
                        
                            form.save()

                            template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat, 'doc':doc, 'ven':ven,})
                            email = EmailMessage(
                                    'Thanks for booking your first dose',
                                    template,
                                    settings.EMAIL_HOST_USER,
                                    [request.user.profile.Email],
                                )

                            email.send()
                                

                            messages.success(request, 'succesfully Updated' )
                                
                            
                            {'form': form}
                

                    
                    return render(request, 'book.html', {'form': form})

                    return redirect('logout')
                            
                else:

                    return redirect('book')

            

            else:

                form = BookForm()
            
                return render(request, 'book.html', {'form':form})
    else:
        return redirect('/venue')





@login_required(login_url='login')
def book_second(request):
    doctors = Doctor.objects.all()
    
    
    doc = random.choice(doctors)
    print(doc)

    # ven = list(Venue.objects.filter(person = request.user).values_list('hospital'))[-1]
    ven =list (Venue.objects.filter(person = request.user).values_list('hospital', flat=True))[-1]
    print(ven)
    
    if request.method == 'POST':
        
        form = Book_SecondForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            
            if len(Book_second.objects.filter(person_id = request.user.id)) == 0:
                print(date)
                instace =form.save(commit = False)
                instace.person = request.user
                instace.save()
                
                dat = date.strftime("%Y-%m-%d")
                print(dat)
                template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat, 'doc':doc, 'ven': ven,})
                email = EmailMessage(
                    'Thanks for booking your second dose ',
                    template,
                    settings.EMAIL_HOST_USER,
                    [request.user.profile.Email],
                )

                email.send()
                

                messages.success(request, 'Successfully booked your second dose')
            else: 
                print(date)

                dat = date.strftime('%b %d %Y')
                bk = Book_second.objects.get(person_id = request.user.id)#.values('date')
                form = Book_SecondForm(request.POST, instance=bk)
                if form.is_valid():
                    form.save
                

                    template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat, 'doc':doc, 'ven': ven,})
                    email = EmailMessage(
                            'Thanks for  booking your second dose',
                            template,
                            settings.EMAIL_HOST_USER,
                            [request.user.profile.Email],
                        )

                    email.send()
                    

                    messages.success(request, 'succesfully Updated your second dose' )
                        
                    
                    {'form': form}


               
            return render(request, 'book_second.html', {'form': form})

            return redirect('logout')
                       
        else:

            return redirect('book_second')

    

    else:

        form = Book_SecondForm()
    
        return render(request, 'book_second.html', {'form':form})



@login_required(login_url='login')
def profile(request):
    # prof = Profile.objects.all
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, files=request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
        
            return redirect ('/venue')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})



@login_required(login_url='login')
def venue(request):
    
    if request.method == 'POST':
        
        form = VenueForm(request.POST)
        
        
        if form.is_valid():

            instace =form.save(commit = False)
            instace.person = request.user
            instace.save()    
                
            
            form.save()

            messages.success(request, 'saved succesfully ' )
        
            return redirect ('/book')
    else:
        form = VenueForm()

    return render(request, 'venue.html', {'form': form})
    



def profile_edit(request, id):
    # if request.method == "GET":
        
        user = User.objects.get(id=id)
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
                form.save()

                return redirect('/dashboard')


        return render (request, 'profile_edit.html', {'form':form})


def dashboard(request):

    prof = Profile.objects.filter(id=request.user.id)
    # prof = Profile.objects.get(request.user.id)
    print('hey')
    print (prof)

    context = {'prof': prof}

     
    return render(request, 'dashboard.html', context)

    

def logout(request):
    auth_logout(request)
    return redirect('')



def mail(request):
    subject ='booking'
    message = 'Thank you for booking'