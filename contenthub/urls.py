from django.urls import path
from . import views

from .apiviews import ContentList, ContentDetail

urlpatterns = [
    path('', views.hompage, name='homepage'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path("contentapi/", ContentList.as_view(), name="content_list"),
    path('contents/', views.contents, name='contents'),
    path("contentapi/<int:pk>/", ContentDetail.as_view(), name="content_detail")
]