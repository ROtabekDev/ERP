from django.db import models

from helpers.models import BaseModel

from apps.employees.models import Employee
from apps.internship.models import Intern


class Attendance(BaseModel):
    """Davomatlar uchun model"""

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances', verbose_name='Xodim',
                                 null=True, blank=True)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name='attendances', verbose_name='Amaliyotchi',
                               null=True, blank=True)
    date = models.DateField('Sanasi')
    arrival_time = models.TimeField('Kelgan vaqti')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Davomat'
        verbose_name_plural = 'Davomatlar'


class MissedTimes(BaseModel):
    """O'tkazib yuborilgan vaqtlar uchun model"""

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='missed_times', verbose_name='Xodim',
                                 null=True, blank=True)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name='missed_times', verbose_name='Amaliyotchi',
                               null=True, blank=True)
    date = models.DateField('Sanasi')
    minutes_late = models.TimeField('Kech qolgan vaqti')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "O`tkazib yuborilgan vaqt"
        verbose_name_plural = "O`tkazib yuborilgan vaqtlar"