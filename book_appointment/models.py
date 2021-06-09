from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=70, blank= False)
    Middle_name = models.CharField(max_length=70)
    Last_name = models.CharField(max_length=70, blank= False)
    #Birthdate = models.DateField(blank= True)
    Occupation = models.CharField(max_length=50, blank= False)
    Email = models.EmailField(max_length= 254)
    #Phone_number = models.IntegerField(blank= True)


    def __str__(self):
        return self.user.username








class Book(models.Model):

    person = models.ForeignKey(User,on_delete=models.CASCADE ,default= None)

    date = models.DateField(null=False)


    # choice = [
    #     ('Very urgent', 'Morning'),
    #     ('Urgent', 'Mid-morning'),
    #     ('Medium', 'Afternoon'),
    #     ('Low', 'Evening'),
    #     ]
    
    # time = models.CharField(max_length= 12, choices= choice, default='urgent')


    # Doctor_Choice =[
    #         ('green','GREEN'),
    #         ('blue', 'BLUE'),
    #         ('red','RED'),
    #         ('orange','ORANGE'),
    #         ('black','BLACK'),
    #     ]


    # doctor = models.CharField(max_length=6, choices= Doctor_Choice, default='green')



    # def __str__(self):
    #     return self.time