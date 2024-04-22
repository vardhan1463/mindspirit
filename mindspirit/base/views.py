from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .form import RoomForms

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


