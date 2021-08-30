

from covid.settings import EMAIL_HOST_USER
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

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
         form = LoginForm(request.POST)
         if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)


            if user is not None:
                form = Loginform()
                login(request, user)

                return redirect('profile')
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
            form.save()
            

            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            

            user = authenticate(username=username, password=password)
            user.save()
            #login(user)
            
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required(login_url='login')
def book(request):
    
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
                template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat})
                email = EmailMessage(
                    'Thanks for booking',
                    template,
                    settings.EMAIL_HOST_USER,
                    [request.user.profile.Email],
                )

                email.send(fail_silently = False)
                email.send()

                messages.success(request, 'Successfully booked')
            else: 
                print(date)

                dat = date.strftime("%Y-%m-%d")
                bk = Book.objects.get(person_id = request.user.id)#.values('date')
                form = BookForm(request.POST, instance=bk)
                form.save()

                template = render_to_string('email.html', {'name':request.user.profile.First_name,'dat':dat})
                email = EmailMessage(
                    'Thanks for booking',
                    template,
                    settings.EMAIL_HOST_USER,
                    [request.user.profile.Email],
                )

                email.send(fail_silently = False)
                email.send()

                messages.info(request, 'succesfully Updated' )
                
               
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
        
            #messages.success(request, 'Your profile has been updated!')

            # data = {
            #     'firstname':firstname,
            #     'email': email,
            #     'subject': subject,
            #     'message': message

            # }
            # message = '''
            # New message:{}

            # From: {}    
                
            #     '''.format(data['message'], data['email'])
            # send_mail(data['subject'], message, '',['tonnycaptain7@gmail.com'])
            return redirect ('/book')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})

def give_vac(request):  
    doctors = Doctor.objects.all()
    lsts = Profile.objects.all()
    clusters = [lsts[person_id:person_id+3] for person_id in range(0, len(lsts), 3)]
    # print (clusters)
    docs = [doctors[id:id+4] for id in range(0, len(doctors), 4)]
    print(docs)
    context= {'clusters': clusters,
                'docs':docs,
    }

    return render(request, 'give_vac.html', context)
    





def logout(request):
    auth_logout(request)
    return redirect('home')



def mail(request):
    subject ='booking'
    message = 'Thank you for booking'