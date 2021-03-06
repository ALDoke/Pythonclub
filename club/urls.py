from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('newResource/', views.newResource, name='newResource'),
    path('newEvent/', views.newEvent, name='newEvent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage')
]