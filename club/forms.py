from django import forms
from .models import Meeting, Resource, Event

class Meetingform(forms.Modelform):
    class Meta:
        model=Meeting
        fields='__all__'

class Resourceform(forms.Modelform):
    class Meta:
        model=Resource
        fields='__all__'

class Eventform(forms.Modelform):
    class Meta:
        model=Event
        fields='__all__'