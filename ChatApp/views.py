from django.shortcuts import render

# Create your views here.

def get_home_page_url(request, *args, **kwargs):
    args = {}
    return render(request, 'chat/index.html', args)


def get_room_url(request, room_name, *args, **kwargs):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })