from django.contrib import admin

# Register your models here.
from .models import Profile, Book, Doctor, Venue

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Doctor)
admin.site.register(Venue)