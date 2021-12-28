from django.urls import path
from . import views
from .views import HomeView, ArticlePage, all_contact

urlpatterns = [
    
    # path('', views.home, name="home"),
    path('searchresults', views.searchresults, name='searchresults'),
    path('', HomeView.as_view(), name='home'),

    path('contactuc.html', views.Contact, name="contactus"),
    path('article/<int:pk>', ArticlePage.as_view(), name='articlepage')
    
]