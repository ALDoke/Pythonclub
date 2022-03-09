from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import Meetingform
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def meetingDetail(request, id):
    meeting-get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting' : meeting})

@login_required
def newMeeting(request):
    form=Meetingform

    if request.method=='POST':
        form=Meetingform(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=Meetingform()
    else:
        form=Meetingform()
    return render(request, 'club/newmeeting.html', {'form': form})

def newResource(request):
    form=Resourceform

    if request.method=='POST':
        form=Resourceform(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=Resourceform()
    else:
        form=Resourceform()
    return render(request, 'club/newresource.html', {'form': form})

def newEvent(request):
    form=Eventform

    if request.method=='POST':
        form=Eventform(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=Eventform()
    else:
        form=Eventform()
    return render(request, 'club/newevent.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')