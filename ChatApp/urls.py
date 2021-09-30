from django.urls import path
from ChatApp import views

urlpatterns = [
    path("", views.get_home_page_url, name="Home"),
    path("welcome-msg/<str:username>/", views.select_user_to_contact, name="Welcome"),
    # path("create-private-chat-room", views.)
    path('<str:room_name>/', views.get_room_url, name='room'),
]
