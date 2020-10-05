from django.urls import path
from . import views

from .apiviews import ContentList, UserCreate, LoginView

urlpatterns = [
    path('', views.hompage, name='homepage'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path("contentapi/", ContentList, name="content_list"),
    path('contents/', views.contents, name='contents'),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("apilogin/", LoginView.as_view(), name="api_login"),
]