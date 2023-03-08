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
    passport = models.ImageField(upload_to='media/images/', null=True, blank=False)
        


    def __str__(self):
        return self.user.username



class Book(models.Model):

    person = models.ForeignKey(User,on_delete=models.CASCADE ,default= None)

    date = models.DateField(null=False)


    def __str__ (self):
        return str(self.person)

class Book_second(models.Model):

    person = models.ForeignKey(User,on_delete=models.CASCADE ,default= None)

    date = models.DateField(null=False)


    def __str__ (self):
        return str(self.person)


class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return str(self.name)


class Venue(models.Model):

    HOSPITAL = (
        ('Kenyatta hsp','KNH-HSP'),
        ('Mbagathi hsp','MGT-HSP'),
        ('Pumwani hsp','PMW-HSP'),
        ('Nairobi hsp','NRB-HSP'),
        ('Kakamega hsp','KKG-HSP'),
        ('Aghakan hsp','AG-HSP'),

    )
    hospital = models.CharField(max_length=30, choices= HOSPITAL, default='NRB')

    person = models.ForeignKey(User,on_delete=models.CASCADE ,default= None)

    def __str__(self):
        return self.hospital

