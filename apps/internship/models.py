from django.db import models

from helpers.models import BaseModel

from apps.employees.models import Gender

from phonenumber_field.modelfields import PhoneNumberField


class Intern(BaseModel):
    """Amaliyotchilar uchun model"""

    first_name = models.CharField('Ismi', max_length=150)
    last_name = models.CharField('Familiyasi', max_length=150)
    phone_number = PhoneNumberField('Telefon raqami', max_length=20)
    direction = models.ForeignKey('Direction', on_delete=models.CASCADE, related_name='interns',
                                  verbose_name='Yo`nalishi')
    birthday = models.DateField('Tug`ilgan sanasi')
    age = models.PositiveIntegerField('Yoshi')
    gender = models.CharField('Jinsi', max_length=15, choices=Gender.choices)
    image = models.ImageField('Rasmi', upload_to='internship/intern/image/',
                              default='internship/intern/image/default-user.png')
    resume_file = models.FileField('CV', upload_to='internship/intern/resume_file/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Amaliyotchi'
        verbose_name_plural = 'Amaliyotchilar'


class Direction(BaseModel):
    """Yo`nalishlar uchun model"""

    title = models.CharField('Nomi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yo`nalish'
        verbose_name_plural = 'Yo`nalishlar'
