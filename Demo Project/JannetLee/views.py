from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'index.html', {})

def contact(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            emailFrom = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])


            form.save()
            try:
                send_mail('New Enquiry', message, emailFrom, ['va.glazing@gmail.com'],fail_silently=False, )
            except BadHeaderError:
                return HttpResponse('Invalid header found')
        return redirect('success')

    return render(request, "contact.html",{'form': form})
    


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
    