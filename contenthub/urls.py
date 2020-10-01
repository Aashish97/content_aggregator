from django.urls import path
from . import views

urlpatterns = [
    path('', views.hompage, name='homepage'),
    path('sharemarket/', views.sharemarket, name='share'),
    path('politics/', views.politics, name='politics'),
    path('gadgets/', views.gadgets, name='gadgets'),
    path('sports/', views.sports, name='sports'),
    path('jobs/', views.jobs, name='jobs'),
]