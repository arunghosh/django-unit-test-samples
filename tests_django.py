import datetime

from django.test import TestCase, Client
from django.utils import timezone

# from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from apps.teachers.models import Availability
from apps.account.models import User
from apps.teachers.models import Teacher
from apps.teachers.apis import AvailabiltyApi

# Using the standard RequestFactory API to create a form POST request


class AvailabilityTestCase(TestCase):
    """
    An example of testing with Django's default TestCase
    """

    def setUp(self):
        """
        Initial method that is common to all test methods.
        This method runs before each test cases. 
        """
        Teacher.objects.register(
            email='teacher@testapi.com',
            first_name='hello',
            last_name='world',
            password='abcd1234')

    def test_01_add_availability(self):
        """
        Initial method that is common to all test methods.
        This method runs after each test cases. 
        """
        login = self.client.login(
            email='teacher@testapi.com', password='abcd1234')
        print login
        a = str(datetime.date(year=2015, month=05, day=02))
        b = str(datetime.date(year=2015, month=05, day=23))

        data = {
            "start_date": str(datetime.date(year=2015, month=05, day=02)),
            "end_date": str(datetime.date(year=2015, month=05, day=23)),
            "start_time": ' '.join(
                [a, str(datetime.time(hour=20, minute=31, second=00))]
            ),
            "end_time": ' '.join(
                [b, str(datetime.time(hour=23, minute=30, second=00))]
            ),
        }
        try:
            response = self.client.post(
                '/api/teachers/availability/', data=data, format='json')
            print 'success'
        except Exception as e:
            print 'error is %s' % e

        print response.status_code
        self.assertEquals(response.status_code, 200)

    
