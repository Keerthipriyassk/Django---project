from django.shortcuts import render
from .models import Room,Message
# Create your views here.
def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html",{
        "rooms":rooms
    })

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    context={"slug":slug,"room_name":room_name,'msgs':messages}
    return render(request, "room.html",context)