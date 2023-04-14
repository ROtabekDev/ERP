from django.db import models

from helpers.models import BaseModel


class ProjectStatus(models.TextChoices):
    New = "new", "Yangi"
    In_progress = 'in_progress', "Jarayonda"
    Finished = "finished", "Tugatilgan"


class ClientType(models.TextChoices):
    Physical_person = "physical_person", "Jismoniy_shaxs"
    Legal_entity = 'legal_entity', "Yuridik shaxs"


class Project(BaseModel):
    """Loyihalar uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='projects', verbose_name='Mijoz')
    project_category = models.ForeignKey('ProjectCategory', on_delete=models.CASCADE, related_name='projects',
                                         verbose_name='Kategoriyasi')
    description = models.TextField('Tavsifi')
    deadline = models.DateField('Tugatish vaqti')
    status = models.CharField('Holati', max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.New)
    price = models.DecimalField('Narxi', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Loyiha'
        verbose_name_plural = 'Loyihalar'


class Client(BaseModel):
    """Mijozlar uchun model"""

    full_name = models.CharField('Ism, familiyasi', max_length=200, null=True, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name='Tashkilot', null=True,
                                     blank=True)
    client_type = models.CharField('Mijoz turi', choices=ClientType.choices)

    def __str__(self):
        return str({self.id})

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'


class Organization(BaseModel):
    """Tashkilotlar uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tashkilot'
        verbose_name_plural = 'Tashkilotlar'


class ProjectCategory(BaseModel):
    """Loyiha kategoriyalari uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Loyiha kategoriyasi'
        verbose_name_plural = 'Loyiha kategoriyalari'
