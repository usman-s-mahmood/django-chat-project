# created manually!
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='chat-index'),
    
]