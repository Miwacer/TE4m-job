from django.contrib import admin
from .models import (
    Worker,
    Task,
    TaskType,
    Position,
)


class AuthorAdmin(admin.ModelAdmin):
    site_header = "Monty Python administration"


admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Worker, AuthorAdmin)