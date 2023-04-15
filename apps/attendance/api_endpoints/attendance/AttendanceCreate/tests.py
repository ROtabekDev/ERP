from django.urls import reverse
from datetime import date
from rest_framework import status
from rest_framework.test import APITestCase
from apps.attendance.models import Attendance
from apps.employees.models import Employee, Position
from apps.internship.models import Intern, Direction


class AttendanceCreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.position = Position.objects.create(
            title='Tean lead :)'
        )

        self.employee = Employee.objects.create(
            first_name='Otabek',
            last_name='Rahmonov',
            phone_number='+998998624122',
            position=self.position,
            birthday='2002-05-22',
            age=20,
            gender='Male',
            salary=5000000.00
        )

        self.direction = Direction.objects.create(
            title='Backend'
        )

        self.intern = Intern.objects.create(
            first_name='Samandar',
            last_name='Rahmonov',
            phone_number='+998901234567',
            direction=self.direction,
            birthday='2005-01-01',
            age=18,
            gender='Male',
        )

    def test_create_attendance(self):
        url = reverse('attendance-create')
        data = {
            'employee': self.employee.id,
            'date': '2023-04-15',
            'arrival_time': '09:30:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Attendance.objects.count(), 1)
        self.assertEqual(Attendance.objects.get(pk=1).employee, self.employee)
        self.assertEqual(Attendance.objects.get(pk=1).date, date.today())
        self.assertEqual(Attendance.objects.get(pk=1).arrival_time.strftime('%H:%M:%S'), '09:30:00')
