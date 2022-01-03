from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomeView, ArticlePage, all_contact, IndexView, AboutPageView, FutureUpdates, contactupdate, Homepage

urlpatterns = [
    
    path('', IndexView.as_view(), name="home"),
    # path('searchresults', views.searchresults, name='searchresults'),
    path('about.html', views.AboutPageView.as_view(), name='About Us'),
    path('bestpractices.html', views.HomeView.as_view(), name='Best Practices'),
    path('futureupdates.html', views.FutureUpdates.as_view(), name='Future Updates'),
    # path('contactuc.html', views.Contact, name="contactus"),
    path('article/<int:pk>', ArticlePage.as_view(), name='articlepage'),
    path('index.html', views.Homepage.as_view(), name='Contact Us'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)