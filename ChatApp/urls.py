from django.urls import path
from ChatApp import views

urlpatterns = [
    path("", views.get_home_page_url, name="Home"),
    path('<str:room_name>/', views.get_room_url, name='room'),
]
