from django.contrib import admin

from .models import Employee, Position, Address, Region, District

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Address)
admin.site.register(Region)
admin.site.register(District)
