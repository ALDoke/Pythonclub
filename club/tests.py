from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Test Meeting')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meetings')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='Test Name')
        self.resource=Resource(resourceurl='http://www.google.com', dateentered='1/1/1111')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Name')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='Test Event')

    def test_Typestring(self):
        self.assertEqual(str(self.type), 'Test Event')

class New_Event_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.type=Type.objects.create(typename='event')
        self.event=Event.objects.create(eventname='event1', user='testuser1')

    def test_redirect_if_not_logged_in(self):
        response.self.client.get(reverse('newevent'))
        self.assertRedirects(response, 'accounts/login/?next=/club/newevent/')