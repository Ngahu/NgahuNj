from django.contrib import admin

from .models import Project, Technology


admin.site.register(Technology)


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'featured',
        'date_created'
    ]


admin.site.register(Project, ProjectAdmin)
