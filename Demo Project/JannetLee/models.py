from django.db import models
from django.contrib.auth.models import User
import datetime
import PIL

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, max_length=32, blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/articles/')
    attack_year = models.IntegerField(('Year of Attack'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, blank=True, null=True)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Contact(models.Model):
    name = models.CharField('name', max_length=30)
    email = models.EmailField('email', max_length=30)
    message = models.TextField('message', max_length=255)
    mobile = models.CharField('phone', max_length=20)
    Type_of_Enquiry = models.TextField('Type_of_Enquiry', max_length=55, blank=True, null=True)

    def __str__(self):
        return self.name

class MyUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    mobile = models.CharField('phone', max_length=20, blank=True, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Enquiry(models.Model):
    name = models.CharField('name', max_length=30)
    email = models.EmailField('email', max_length=30)
    mobile = models.CharField('phone', max_length=20)
    Type_of_Enquiry = models.TextField('Type_of_Enquiry', max_length=55, blank=True, null=True)
    message = models.TextField('message', max_length=255)
    attendees = models.ManyToManyField(MyUser, blank=True, null=True)

    def __str__(self):
        return self.name 



