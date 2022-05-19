from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, CreatorPageView
urlpatterns = [
    # path('', views.index, name='index')
     path("creator/", CreatorPageView.as_view(), name="creator"),
     path("about/", AboutPageView.as_view(), name="about"),
     path("", HomePageView.as_view(), name="home"),
]