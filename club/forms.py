from django import forms
from .models import Meeting, Resource, Event

class Meetingform(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class Resourceform(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'

class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'