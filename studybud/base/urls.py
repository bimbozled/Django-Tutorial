from django.urls import path
from . import views

## this line below had a error for commits 2 and 3, fixed with chatgpt. 
urlpatterns = [
    path('',views.home,name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),


]
