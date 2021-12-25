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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/articles/')
    category = models.CharField(max_length=255, default="uncategorized")
    attack_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, blank=True, null=True)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)