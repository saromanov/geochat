import random
from django.test import TestCase
from .models import Message
from django.contrib.gis.geos import Point

def create_message(long, lat):
    ''' generate random text message
    '''
    text = "".join( [random.choice(string.letters) for i in xrange(15)] )
    Message.objects.create(text=text, geometry=Point(long, lat), user_id=3)

class MessageModelTest(TestCase):
    def test_messages_without_point(self):
        m = Message(text='Yes0')
        self.assertIs(m.__str__(), 'Yes0')
