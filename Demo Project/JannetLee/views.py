from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'contactus.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Enquiry = request.POST['Enquiry']
        message = request.POST['message']

        # sned an email 
        send_mail(
            'name', # subject 
            'message', # message 
            'email', # from email 
            ['jianyi2021@gmail.com'], # to Email
        )

        return render(request, 'contactus.html', {'name' : name })

    else:
        return render(request, 'contactus.html', {})
    # contact = Post.objects.all()
    # return render(request, 'template/aboutus.html', {'aboutus' : aboutus })
    


def searchresults(request): #https://www.youtube.com/watch?v=AGtae4L5BbI, to be continued (13:46)
    if request.method == "POST":
        searched = request.POST["searched"] # if user has inputed, return the input
        articles = Post.objects.filter(title__contains=searched)

        return render(request, 'searchresults.html', {"searched":searched, "articles":articles})
    else:
        return render(request, 'searchresults.html', {})

# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
    