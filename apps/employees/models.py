from django.db import models

from helpers.models import BaseModel


class Gender(models.TextChoices):
    Male = "Male", "Erkak"
    Female = "Female", "Ayol"


class Employee(BaseModel):
    """Xodimlar uchun model"""

    first_name = models.CharField('Ismi', max_length=150)
    last_name = models.CharField('Familiyasi', max_length=150)
    phone_number = models.CharField('Telefon raqami', max_length=20)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='employees',
                                 verbose_name='Lavozimi')
    birthday = models.DateField('Tug`ilgan sanasi')
    age = models.PositiveIntegerField('Yoshi')
    gender = models.CharField('Jinsi', max_length=15, choices=Gender.choices)
    image = models.ImageField('Rasmi', upload_to='employees/employee/image/',
                              default='employees/employee/image/default-user.png')
    resume_file = models.FileField('CV', upload_to='employees/employee/resume_file/')
    salary = models.DecimalField('Maoshi', max_digits=10, decimal_places=2)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'


class Position(BaseModel):
    """Lavozimlar uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lavozim'
        verbose_name_plural = 'Lavozimlar'


class Address(BaseModel):
    """Manzillar uchun model"""

    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='addresses', verbose_name='Viloyati')
    district = models.ForeignKey('District', on_delete=models.CASCADE, related_name='addresses', verbose_name='Tumani')
    home_address = models.CharField('Uy manzili', max_length=250)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Manzil'
        verbose_name_plural = 'Manzillar'


class Region(BaseModel):
    """Viloyat/Shaharlar uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Viloyat/Shahar'
        verbose_name_plural = 'Viloyat/Shaharlar'


class District(BaseModel):
    """Tuman/Shaharlar uchun model"""

    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='districts', verbose_name='Viloyati')
    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tuman/Shahar'
        verbose_name_plural = 'Tuman/Shaharlar'
