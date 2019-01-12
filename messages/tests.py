from django.test import TestCase
from .models import Message

class MessageModelTest(TestCase):
    def test_messages_without_point(self):
        m = Message(text='Yes0')
        self.assertIs(m.__str__(), 'Yes0')
