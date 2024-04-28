from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room,topic,message
from .form import RoomForms


# rooms = [ 
#     {'id':1,'name':'learn pythomn'},
#     {'id':2,'name':'learn shell'},
#     {'id':3,'name':'learn java'},
# ]

def homemain(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)| 
        Q(name__icontains=q) | 
        Q(description__icontains=q)
    )
    Topic =topic.objects.all()
    room_count=rooms.count()
    room_messages=message.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms': rooms,'topics':Topic,'room_count':room_count,'room_messages':room_messages}
    return render(request,'base/home.html', context)

def userProfile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    room_messages=user.message_set.all()
    topics =topic.objects.all()
    context={'user':user,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')  
        else:
            messages.error(request,'Username OR Password does not exist')
    context={'page':page}
    return render(request,'base/login_register.html',context)

def logoutuser(request):
    logout(request)
    return redirect('home')

def registeruser(request):
    page='register'
    form=UserCreationForm()
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request.user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')

    return render(request,'base/login_register.html',{'form':form})

def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages=room.message_set.all().order_by('-created')
    participants=room.participants.all()
    if request.method == 'POST':
        new_message =message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def deletemessage(request,pk):
    Message=message.objects.get(id=pk)

    if request.user != Message.user:
        return HttpResponse('You are not allowed here!!')
    
    if request.method=='POST':
        Message.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':Message})

@login_required(login_url='login')
def create_room(request):
    form = RoomForms()
    # topics=topic.objects.all()
    if request.method=='POST':
        
        form=RoomForms(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()
            
        return redirect('home')        
    context={'form':form,}    
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def updateroom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForms(instance=room)
    # topics=topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method=='POST':
        form=RoomForms(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form':form,}
    return render(request,'base/create_room.html',context)

@login_required(login_url='login')
def deleteroom(request,pk):
    room=Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url='login')
def updateUser(request):
    return render(request,'base/update-user.html')
       

