from django.db import models

from helpers.models import BaseModel


class Equipment(BaseModel):
    """Jihozlar uchun model"""

    equipment_name = models.ForeignKey('EquipmentName', on_delete=models.CASCADE, related_name='equipments',
                                       verbose_name='Jihoz nomi')
    equipment_category = models.ForeignKey('EquipmentCategory', on_delete=models.CASCADE, related_name='equipments',
                                           verbose_name='Jihoz kategoriyasi')
    price = models.DecimalField('Narxi', max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField('Soni', default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Jihoz'
        verbose_name_plural = 'Jihozlar'


class EquipmentName(BaseModel):
    """Jihoz nomlari uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Jihoz nomi'
        verbose_name_plural = 'Jihoz nomlari'


class EquipmentCategory(BaseModel):
    """Jihoz kategoriyalari uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Jihoz kategoriyasi'
        verbose_name_plural = 'Jihoz kategoriyalari'
