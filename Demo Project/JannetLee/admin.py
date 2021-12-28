from django.contrib import admin
from .models import Post, Category, Enquiry, MyUser

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Enquiry)
admin.site.register(MyUser)
