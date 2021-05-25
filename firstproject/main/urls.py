from django.urls import path
from . import views #import from this directiry

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about')
]
