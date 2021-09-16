

from covid.settings import EMAIL_HOST_USER
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
import random

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout as auth_logout 
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BookForm
from book_appointment.forms import SignUpForm, BookForm, ProfileForm
from .models import Book, Doctor, Profile
from django.core.mail import  send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def homepage(request):
    
    return render(request, 'home.html')


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

                return redirect('profile')
                
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
            messages.success(request, "Registered successfuly.")
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Information is invalid.")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required(login_url='login')
def book(request):
    doctors = Doctor.objects.all()
    
    # d = random.randrange(len(doctors))
    # doc = doctors[d]
    doc = random.choice(doctors)
    print(doc)
    
    
    
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
                template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat, 'doc':doc})
                email = EmailMessage(
                    'Thanks for booking',
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
                form.save()

                template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat, 'doc':doc})
                email = EmailMessage(
                    'Thanks for booking',
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




@login_required(login_url='login')
def profile(request):
    #form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST, files=request.FILES, instance = request.user.profile,)
        if form.is_valid():
            form.save()
        
            return redirect ('/book')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})

# def give_vac(request):  
#     doctors = Doctor.objects.all()
#     # lasts = Profile.objects.all()
#     # clusters = [lsts[person_id:person_id+3] for person_id in range(0, len(lsts), 3)]
#     # print (clusters)
#     docs = [doctors[id:id+4] for id in range(0, len(doctors), 4)]
#     print(docs)
#     context= {'clusters': clusters,
#                 'docs':docs,
#     }

#     return render(request, 'give_vac.html', context)
    





def logout(request):
    auth_logout(request)
    return redirect('')



def mail(request):
    subject ='booking'
    message = 'Thank you for booking'