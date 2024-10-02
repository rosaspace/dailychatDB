from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/conversation', views.get_conversation, name='get_conversation'),
]