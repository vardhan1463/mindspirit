from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.registeruser,name='register'),
    path('',views.homemain,name='home'),
    path('room/<str:pk>',views.room,name='room'),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
    path('create_room/',views.create_room,name='create_room'),
    path('Update_room/<str:pk>/',views.updateroom,name='update-room'),
    path('delete_room/<str:pk>/',views.deleteroom,name='delete-room'),
    path('delete_message/<str:pk>/',views.deletemessage,name='delete-message'),
    path('update-user/<str:pk>/',views.updateUser,name='update-user'),
]