from django.db import models
from django.contrib.auth.models import User
import PIL

class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/articles/')

    def __str__(self):
        return self.title + ' | ' + str(self.author)