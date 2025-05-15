from django.contrib import admin
from .models import (
    Worker,
    Task,
    TaskType,
    Position,
    Team,
    Project,
)


class AuthorAdmin(admin.ModelAdmin):
    site_header = "Monty Python administration"


admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Worker, AuthorAdmin)