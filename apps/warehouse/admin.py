from django.contrib import admin

from .models import Equipment, EquipmentName, EquipmentCategory

admin.site.register(Equipment)
admin.site.register(EquipmentName)
admin.site.register(EquipmentCategory)
