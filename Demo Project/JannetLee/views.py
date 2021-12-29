from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Contact
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# def home(request):
#     return render(request, 'bestpractices.html', {})
def all_contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus?submitted=True')

    else: 
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'enquirylist.html', 
            {'form' : form, 'submitted': submitted})



def searchresults(request): #https://www.youtube.com/watch?v=AGtae4L5BbI, to be continued (13:46)
    if request.method == "POST":
        searched = request.POST["searched"] # if user has inputed, return the input
        articles = Post.objects.filter(title__contains=searched)

        return render(request, 'searchresults.html', {"searched":searched, "articles":articles})
    else:
        return render(request, 'searchresults.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'about.html'

class ArticlePage(DetailView):
    model = Post
    template_name = 'articlepage.html'
    