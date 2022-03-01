from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

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