from email import message
from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def rooms(request):

    rooms = Room.objects.all()

    context = {
        'rooms':rooms
    }

    return render(request, 'rooms.html',context)

#Room details

@login_required
def room(request, slug):

    room = Room.objects.get(slug=slug)

    messages = Message.objects.filter(room=room)[0:25]

    context = {
        'room':room,
        'messages':messages
    }

    return render(request, 'roomdet.html', context)