from django.shortcuts import render


def index(request):
    return render(request, 'messenger/index.html')


def room(request, room_name, token):
    context = {'room_name': room_name, 'token': token}
    return render(request, 'messenger/room.html', context)
