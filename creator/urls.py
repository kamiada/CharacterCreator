from django.urls import path
from . import views
from .views import HomePageView, AboutPageView
urlpatterns = [
    # path('', views.index, name='index')
     path("about/", AboutPageView.as_view(), name="about"),
     path("", HomePageView.as_view(), name="home"),
]