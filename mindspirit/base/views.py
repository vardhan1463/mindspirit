from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,topic
from .form import RoomForms
from django.db.models import Q
# rooms = [ 
#     {'id':1,'name':'learn pythomn'},
#     {'id':2,'name':'learn shell'},
#     {'id':3,'name':'learn java'},
# ]
# Create your views here.
def home(request):
    return HttpResponse('home page')

def homemain(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)| 
        Q(name__icontains=q) | 
        Q(description__icontains=q)
    )
    Topic =topic.objects.all()
    room_count=rooms.count()
    context = {'rooms': rooms,'topics':Topic,'room_count':room_count}
    return render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)

def create_room(request):
    form = RoomForms()
    if request.method=='POST':
        form=RoomForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')        
    context={'form':form}    
    return render(request,'base/create_room.html',context)

def updateroom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForms(instance=room)
    if request.method=='POST':
        form=RoomForms(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/create_room.html',context)

def deleteroom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})
       

