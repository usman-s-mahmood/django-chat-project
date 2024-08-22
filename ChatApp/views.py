from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(
        request,
        'ChatApp/home.html',
        {
            
        }
    )
    
def room(request, room):
    username = request.GET.get('username')
    room_details = models.Room.objects.get(name=room)
    return render(
        request,
        'ChatApp/room.html',
        {
            'username': username,
            'room_details': room_details,
            'room': room
        }
    )
    
def checkView(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if models.Room.objects.filter(name=room).exists():
        return redirect('/'+room, '/?username='+ username)
    else:
        models.Room.objects.create(
            name=room
        ).save()
        return redirect('/'+room, '/?username='+ username)

def send(request):
    message = request.POST['message']
    username = request.POST['username'],
    room_id = request.POST['room_id']
    room = models.Room.objects.filter(id=room_id).first();
    models.Message.objects.create(
        value=message,
        room=room
    ).save()
    return render(
        request
    )
    
    return HttpResponse('Message Sent!')

def getMessages(request, room):
    room_details = models.Room.objects.get(name=room)
    messages = models.Message.objects.filter(
        room=room
    )
    return JsonResponse(
        {
            'messages': list(messages.values())
        }
    )