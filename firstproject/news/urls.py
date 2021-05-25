from django.urls import path
from . import views #import from this directory

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create')
]
