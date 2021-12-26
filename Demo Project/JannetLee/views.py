from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'contactus.html', {})

def contact(request,):
    if request.method == "POST":
        message_name = request.POST['message-name']
        Your_email = request.POST['email']
        Your_phone = request.POST['phone']
        Enquiry = request.POST['Enquiry']
        message = request.POST['message']

        # send an email 
        send_mail(
            message_name, # subject 
            message, # message 
            Your_email, # from email 
            ['jianyi2021@gmail.com'], # to Email
        )

        return render(request, 'contactus.html', {'message_name' : message_name })

    else:
        return render(request, 'contactus.html', {})
    # contact = Post.objects.all()
    # return render(request, 'template/aboutus.html', {'aboutus' : aboutus })
    


def searchresults(request): #https://www.youtube.com/watch?v=AGtae4L5BbI, to be continued (09:44)
    if request.method == "POST":
        searched = request.POST["searched"]
        return render(request, 'searchresults.html', {"searched":searched})
    else:
        return render(request, 'searchresults.html', {})

# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
    