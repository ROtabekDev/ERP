from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.attendance.models import Attendance
from apps.employees.models import Employee, Position
from .serializers import AttendanceListSerializer


class AttendanceTests(APITestCase):

    def setUp(self):
        self.position1 = Position.objects.create(
            title='Tean lead :)'
        )
        self.position2 = Position.objects.create(
            title='Backend developer'
        )

        self.employee1 = Employee.objects.create(
            first_name='Otabek',
            last_name='Rahmonov',
            phone_number='+998998624122',
            position=self.position1,
            birthday='2002-05-22',
            age=20,
            gender='Male',
            salary=5000000.00
        )

        self.employee2 = Employee.objects.create(
            first_name='Samandar',
            last_name='Rahmonov',
            phone_number='+998901234567',
            position=self.position2,
            birthday='2005-01-01',
            age=18,
            gender='Male',
            salary=3000000.00
        )

        self.attendance1 = Attendance.objects.create(
            employee=self.employee1,
            date='2023-04-15',
            arrival_time='09:30:00'
        )
        self.attendance2 = Attendance.objects.create(
            employee=self.employee2,
            date='2023-04-15',
            arrival_time='09:30:00'
        )

    def test_get_attendance_list(self):
        url = reverse('attendance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Attendance.objects.count(), 2)

    def test_get_attendance_list_by_date(self):
        url = reverse('attendance-list')
        date = self.attendance1.date
        response = self.client.get(url, {'date': date})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AttendanceListSerializer(Attendance.objects.filter(date=date), many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_get_attendance_list_by_employee(self):
        url = reverse('attendance-list')
        employee_id = self.attendance1.employee_id
        response = self.client.get(url, {'employee': employee_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AttendanceListSerializer(Attendance.objects.filter(employee_id=employee_id), many=True).data
        self.assertEqual(response.data, serializer_data)
