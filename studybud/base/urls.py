from django.urls import path
from . import views

## this line below had a error for commits 2 and 3, fixed with chatgpt. 
urlpatterns = [
    path('',views.home,name="home"),
    path('room/<str:pk>/', views.room, name="room"),

]
