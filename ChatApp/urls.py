# created manually!
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='chat-index'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkView, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')
]