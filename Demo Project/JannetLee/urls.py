from django.urls import path
from . import views
from .views import HomeView, ArticlePage, all_contact, IndexView, AboutPageView, FutureUpdates

urlpatterns = [
    
    path('', IndexView.as_view(), name="home"),
    # path('searchresults', views.searchresults, name='searchresults'),
    path('about.html', views.AboutPageView.as_view(), name='About Us'),
    path('bestpractices.html', views.HomeView.as_view(), name='Best Practices'),
    path('futureupdates.html', views.FutureUpdates.as_view(), name='Future Updates'),
    # path('contactuc.html', views.Contact, name="contactus"),
    path('article/<int:pk>', ArticlePage.as_view(), name='articlepage')

]