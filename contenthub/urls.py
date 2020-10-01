from django.urls import path
from . import views

urlpatterns = [
    path('', views.hompage, name='homepage'),
    path('contents/', views.contents, name='contents'),
]