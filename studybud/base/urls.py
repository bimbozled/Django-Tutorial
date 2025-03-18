from django.urls import path
from . import views

## this line below had a error for commits 2 and 3, fixed with chatgpt. 
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),


    path('',views.home,name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    path('update-user/<str:pk>', views.updateUser, name='update-user'),


]
