from django.urls import path
from .import views

urlpatterns = [
    path('',views.homemain),
    path('home',views.home),
    path('room/<str:pk>',views.room,name='room'),
]