from django.contrib import admin
from .models import Task

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('task',)
