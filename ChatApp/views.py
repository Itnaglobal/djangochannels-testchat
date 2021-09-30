from ChatApp.models import PrivateChtRoom
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def get_home_page_url(request, *args, **kwargs):
    users = User.objects.exclude(username=request.user)
    args = {
        'users': users
    }
    return render(request, 'chat/index.html', args)


def welcome_msg_from_user(request, *args, **kwargs):
    return render(request, 'chat/welcomemsg.html')



def select_user_to_contact(request, username, *args, **kwargs):
    user2 = User.objects.get(username=username)
    user = request.user
    room_name = request.POST.get('room_name')

    if user.is_authenticated:
        if request.method == "POST":
            room = PrivateChtRoom(
                user1=user,
                user2=user2,
                room_name=room_name
            )
            room.save()

            return redirect(f"/chat/{room.room_name}")

    args = {
        "user2": user2
    }

    return render(request, 'chat/welcomemsg.html', args)


def get_room_url(request, room_name, *args, **kwargs):
    args = {
        'room_name': room_name
    }
    return render(request, 'chat/room.html', args)
