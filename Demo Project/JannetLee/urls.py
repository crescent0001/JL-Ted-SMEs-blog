from django.urls import path
from . import views
from .views import HomeView, ArticlePage

urlpatterns = [
    # path('', views.home, name="home"),
    path('searchresults', views.searchresults, name='searchresults'),
    path('', HomeView.as_view(), name='home'),
    path('contactus.html', views.contact, name="contactus"),
    path('article/<int:pk>', ArticlePage.as_view(), name='articlepage')
    
]