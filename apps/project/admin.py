from django.contrib import admin

from .models import Project, Client, Organization, ProjectCategory

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Organization)
admin.site.register(ProjectCategory)
