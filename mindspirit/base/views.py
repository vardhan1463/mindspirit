from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [ 
#     {'id':1,'name':'learn pythomn'},
#     {'id':2,'name':'learn shell'},
#     {'id':3,'name':'learn java'},
# ]
# Create your views here.
def home(request):
    return HttpResponse('home page')

def homemain(request):
    rooms=Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)