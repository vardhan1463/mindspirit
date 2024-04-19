from django.shortcuts import render
from django.http import HttpResponse

rooms = [ 
    {'id':1,'name':'learn pythomn'},
    {'id':2,'name':'learn shell'},
    {'id':3,'name':'learn java'},
]
# Create your views here.
def home(request):
    return HttpResponse('home page')

def homemain(request):
    context = {'rooms': rooms}
    return render(request,'base/home.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room=i
    context={'room':room}
    return render(request,'base/room.html',context)