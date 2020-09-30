from django.urls import path
from . import views

urlpatterns = [
    path('', views.hompage, name='homepage'),
    path('sharemarket/', views.sharemarket, name='share'),
    path('politics/', views.politics, name='politics'),
]