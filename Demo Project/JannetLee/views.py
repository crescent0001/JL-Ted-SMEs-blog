from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from .models import Post

def home(request):
    return render(request, 'bestpractices.html', {})

def searchresults(request): #https://www.youtube.com/watch?v=AGtae4L5BbI, to be continued (09:44)
    if request.method == "POST":
        searched = request.POST["searched"]
        return render(request, 'searchresults.html', {"searched":searched})
    else:
        return render(request, 'searchresults.html', {})

# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
    