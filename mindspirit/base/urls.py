from django.urls import path
from .import views

urlpatterns = [
    path('',views.homemain,name='home'),
    path('home',views.home),
    path('room/<str:pk>',views.room,name='room'),
    path('create_room/',views.create_room,name='create_room'),
    path('Update_room/<str:pk>/',views.updateroom,name='update-room'),
    path('delete_room/<str:pk>/',views.deleteroom,name='delete-room'),
]