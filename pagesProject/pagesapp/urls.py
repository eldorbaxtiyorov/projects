from django.urls import path
from .views import HomePageView, AboutPageView, NewsPageView, FounderPageView

urlpatterns = [
    path('founder/', FounderPageView.as_view(), name='founder'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')]
