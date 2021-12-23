from django.urls import path
from . import views
# from .views import HomeView

urlpatterns = [
    path('', views.home, name="home"),
    path('searchresults', views.searchresults, name='searchresults'),
    # path('', HomeView.as_view(), name='home'),
]